import React from 'react';
import { Link } from 'react-router-dom';
import PanToolIcon from '@material-ui/icons/PanTool';
import { makeStyles } from '@material-ui/core';
const useStyles = makeStyles({
    root: {
      justifyContent: "center",
      textAlign: "center",
      color: "maroon",
    },
    link: {
        backgroundColor: "maroon",
        borderRadius: "25px",
        padding: "10px",
        '&:hover': {
            backgroundColor: "lightSalmon",
        },
        color: "white",
        textDecoration: "none"
    },
    icon: {
        padding : "20px",
    }
  });
const NotFound = () => {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <h1><PanToolIcon classname={classes.icon}/> 404 <PanToolIcon classname={classes.icon}/> </h1>
            <p>Page Not Found</p>
            <Link className={classes.link} to="/">Return to HomePage</Link>
        </div>
    );
};

export default NotFound;