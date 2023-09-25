/** @type {import('next').NextConfig} */
const nextConfig = {}
const path = require('path')


module.exports = {
/* Add Your Scss File Folder Path Here */
sassOptions: {
includePaths: [path.join(__dirname, 'Style')],
},  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/,
      use: ["@svgr/webpack"],
      options: {
        native: true,
      },
      
    });

    return config;
  },
}
module.exports = nextConfig
