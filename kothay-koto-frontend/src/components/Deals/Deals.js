import React, { useEffect, useState } from 'react';
import SingleCard from '../SingleCard/SingleCard';
import { makeStyles, Grid, Typography } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        padding: theme.spacing(2),
        marginLeft: '80px',
    }
}))
const Deals = () => {
    const classes = useStyles();
    const [deal, setDeal] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000')
        .then(res => res.json())
        .then(data => {
            setDeal(data);
        })
        .catch(err => console.log(err))
    } ,[])
    console.log(deal[0]);
    return (
        <div className={classes.root}>
            <Typography variant="h4" gutterBottom>
                Best Deals Right Now!
            </Typography>
            <Grid
                container
                spacing={2}
                direction="row"
                justify="flex-start"
                alignItems="flex-start"
            >
                
                <Grid item xs={12} sm={6} md={3}>
                {deal && deal.map(pd => <SingleCard product={pd}></SingleCard>)}
                
                </Grid>
                
            </Grid>
        </div>
    );
};

export default Deals;