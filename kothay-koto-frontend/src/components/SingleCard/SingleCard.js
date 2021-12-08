import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import img from "../../Images/product-3.png";
const useStyles = makeStyles({
    root: {
      maxWidth: 345,
    },
    price: {
        color: "maroon",
        fontWeight: 600,
    }
  });
  
const SingleCard = (props) => {
    console.log(props.product);
    const {Vendor,Name,PictureUri,Price,Description,ProductUri} = props;
    const classes = useStyles();
    return (
        <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="250"
          image={PictureUri}
          title="laptop"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {Name}
          </Typography>
          <Typography className = {classes.price}>
            {Price}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p" gutterBottom>
          {Description}
          </Typography>
          <Typography variant="body2" color="primary" component="p">
          {Vendor}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Add to Wishlist
        </Button>
        <Button size="small" color="primary" href={ProductUri}>
          Go to Site
        </Button>
      </CardActions>
    </Card>
    );
};

export default SingleCard;