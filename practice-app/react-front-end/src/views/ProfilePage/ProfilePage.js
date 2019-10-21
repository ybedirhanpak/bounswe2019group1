import React, { useState } from "react";
// nodejs library that concatenates classes
import classNames from "classnames";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// @material-ui/icons
import Camera from "@material-ui/icons/Camera";
//import Palette from "@material-ui/icons/Palette";
//import Button from "components/CustomButtons/Button.js";

import Event from "@material-ui/icons/Event";
import Favorite from "@material-ui/icons/Favorite";
// core components
import Header from "components/Header/Header.js";
import Footer from "components/Footer/Footer.js";
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import HeaderLinks from "components/Header/HeaderLinks.js";
import NavPills from "components/NavPills/NavPills.js";
import Parallax from "components/Parallax/Parallax.js";
import { Link } from "react-router-dom";
import profile from "assets/img/faces/ai.jpg";

import portfolio1 from "assets/img/examples/studio-1.jpg";
import portfolio2 from "assets/img/examples/studio-2.jpg";
import portfolio3 from "assets/img/examples/studio-3.jpg";
import portfolio4 from "assets/img/examples/studio-4.jpg";
import portfolio5 from "assets/img/examples/studio-5.jpg";
import event1 from "assets/img/examples/olu-eletu.jpg";
import event2 from "assets/img/examples/clem-onojeghuo.jpg";
import event3 from "assets/img/examples/cynthia-del-rio.jpg";
import event4 from "assets/img/examples/mariya-georgieva.jpg";
import event5 from "assets/img/examples/clem-onojegaw.jpg";

import styles from "assets/jss/material-kit-react/views/profilePage.js";
import { getProfileInfo } from "../../service/profileinformation.service";
// import {getProfileInfo} from "../../service/getProfileInformation";

const useStyles = makeStyles(styles);

export default function ProfilePage(props) {
  const classes = useStyles();
  const { ...rest } = props;
  const [profileValues, setProfileValues] = useState({
    first_name: "",
    last_name: ""
  });
  const imageClasses = classNames(
    classes.imgRaised,
    classes.imgRoundedCircle,
    classes.imgFluid
  );
  getProfileInfo().then(res =>
    setProfileValues({ first_name: res.first_name, last_name: res.last_name })
  );
  const navImageClasses = classNames(classes.imgRounded, classes.imgGallery);
  return (
    <div>
      <Link to="/">
      <Header
        color="transparent"
        brand="Khaji-it Traders Platform"
        rightLinks={<HeaderLinks />}
        fixed
        changeColorOnScroll={{
          height: 200,
          color: "white"
        }}
        {...rest}
      /></Link>
      <Parallax small filter image={require("assets/img/dollar-hd.jpg")} />
      <div className={classNames(classes.main, classes.mainRaised)}>
        <div>
          <div className={classes.container}>
            <GridContainer justify="center">
              <GridItem xs={12} sm={12} md={6}>
                <div className={classes.profile}>
                  <div>
                    <img src={profile} alt="..." className={imageClasses} />
                  </div>

                  <div className={classes.name}>
                    <h3 className={classes.title}>
                      {profileValues.first_name} {profileValues.last_name}
                    </h3>
                    <h6>ECONOMIST</h6>
                  </div>
                </div>
              </GridItem>
            </GridContainer>
            <div className={classes.description}>
              <p>
                23 years old, Lives in İstanbul, Graduated from Boğaziçi
                University, Department of Economics.{" "}
              </p>
            </div>
            <GridContainer justify="center">
              <GridItem xs={12} sm={12} md={8} className={classes.navWrapper}>
                <NavPills
                  alignCenter
                  color="primary"
                  tabs={[
                    {
                      tabButton: "Portfolios",
                      tabIcon: Camera,
                      tabContent: (
                        <GridContainer justify="center">
                          <GridItem xs={12} sm={12} md={4}>
                            <img
                              alt="..."
                              src={portfolio1}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={portfolio2}
                              className={navImageClasses}
                            />
                          </GridItem>
                          <GridItem xs={12} sm={12} md={4}>
                            <img
                              alt="..."
                              src={portfolio5}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={portfolio4}
                              className={navImageClasses}
                            />
                          </GridItem>
                        </GridContainer>
                      )
                    },
                    {
                      tabButton: "Events",
                      tabIcon: Event,
                      tabContent: (
                        <GridContainer justify="center">
                          <GridItem xs={12} sm={12} md={4}>
                            <img
                              alt="..."
                              src={event1}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={event2}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={event3}
                              className={navImageClasses}
                            />
                          </GridItem>
                          <GridItem xs={12} sm={12} md={4}>
                            <img
                              alt="..."
                              src={event4}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={event5}
                              className={navImageClasses}
                            />
                          </GridItem>
                        </GridContainer>
                      )
                    },
                    {
                      tabButton: "Likes",
                      tabIcon: Favorite,
                      tabContent: (
                        <GridContainer justify="center">
                          <GridItem xs={12} sm={12} md={4}>
                            <img
                              alt="..."
                              src={event4}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={portfolio3}
                              className={navImageClasses}
                            />
                          </GridItem>
                          <GridItem xs={12} sm={12} md={4}>
                            <img
                              alt="..."
                              src={event2}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={event1}
                              className={navImageClasses}
                            />
                            <img
                              alt="..."
                              src={portfolio1}
                              className={navImageClasses}
                            />
                          </GridItem>
                        </GridContainer>
                      )
                    }
                  ]}
                />
              </GridItem>
            </GridContainer>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}