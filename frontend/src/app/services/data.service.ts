import { Injectable } from '@angular/core';
import { HttpClient, HttpEventType } from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  url = 'http://10.159.44.185:8080/'

  constructor(private http: HttpClient) { }

  contextSearch(query: string = '', sort_by: string, sort_order: number, filetype: string) {
    let request = '?'
    if(query.trim().length) {
      request = request+'query='+query
      request = request+'&sort_by='+sort_by+'&sort_order='+sort_order
    } else {
      request = request+'sort_by='+sort_by+'&sort_order='+sort_order
    }
    
    if(filetype.trim().length) {
      request = request+'&filetype='+filetype
    }

    this.http.get(this.url+"search"+request).subscribe((response: any) => {
      debugger
      return response
    })
  }

  imageSearch(file: any) {
    const formData = new FormData();
    formData.append('file', file, file.name);

    this.http.post(this.url+'/uploadfile', formData, {
        reportProgress: true,
        observe: 'events'
      })
      .subscribe((event: any) => {
        return event
      });
  }

  downloadFile(fileName: string) {
    this.http.get(this.url+'getfile'+'?filename='+fileName, {responseType: 'blob' as 'json'}).subscribe((file: any) => {
      let blob = new Blob([file], {type: file.type});
      var downloadURL = window.URL.createObjectURL(blob);
      var link = document.createElement('a');
      link.href = downloadURL;
      link.download = fileName;
      link.click();
    })
    // You should replace this with your actual file download logic.
    // For demonstration purposes, we'll create a dummy download link.
    
    // // Create an anchor element for downloading the file.
    // const link = document.createElement('a');
    
    // // Set the anchor's href attribute to the file URL.
    // link.href = this.url+fileName;
    
    // // Specify the download attribute to suggest a file name for the downloaded file.
    // link.download = fileName;
    
    // // Trigger a click event to initiate the download.
    // link.click();
    
    // // Cleanup: Remove the anchor element from the DOM.
    // document.body.removeChild(link);
  }

  getFiles() {
    query: [
      {
        date: 'Tue Oct 11 07:16:14 2011',
        name: 'Carlson.Anderson.acq0001.jpg',
        type: 'jpg',
        rank: '1'
      },
      {
        date: 'Thu Apr 22 11:43:50 2010',
        name: 'Beith.kids.arch.jpg',
        type: 'jpg',
        rank: '2'
      },
      {
        date: 'Mon Jan 18 11:24:16 2021',
        name: 'Kobayashi Video Final.mp4',
        type: 'mp4',
        rank: '3'
      },
      {
        date: 'Tue Mar 16 11:57:42 2004',
        name: 'alligator pit.jpg',
        type: 'jpg',
        rank: '4'
      },
      {
        date: 'Tue Oct  3 12:05:46 2023',
        name: 'Screenshot 2023-10-03 140547.png',
        type: 'png',
        rank: '5'
      },
      {
        date: 'Thu Mar  6 13:12:28 2014',
        name: 'VillaGarden.1pghistory.doc',
        type: 'doc',
        rank: '6'
      },
      {
        date: 'Tue Jul 25 14:37:18 2023',
        name: 'Shakespeare_trial_1916.jpg',
        type: 'jpg',
        rank: '7'
      },
      {
        date: 'Mon Apr 18 11:26:26 2011',
        name: 'Leverty.coll.Villagate.jpg',
        type: 'jpg',
        rank: '8'
      },
      {
        date: 'Mon Jun 18 11:12:38 2012',
        name: '2012.kidsdaypgm.bkmk.doc',
        type: 'doc',
        rank: '9'
      },
      {
        date: 'Wed Aug 25 09:52:18 2004',
        name: 'cutiepie.jpg',
        type: 'jpg',
        rank: '10'
      },
      {
        date: 'Tue Jun 13 09:06:48 2000',
        name: 'SIGNIFICANT BUILDINGS.doc',
        type: 'doc',
        rank: '11'
      },
      {
        date: 'Tue Oct  3 12:06:02 2023',
        name: 'Screenshot 2023-10-03 140603.png',
        type: 'png',
        rank: '12'
      },
      {
        date: 'Thu Jun  7 10:10:34 2007',
        name: 'RALwinter.jpg',
        type: 'jpg',
        rank: '13'
      },
      {
        date: 'Tue Jun 20 10:54:38 2023',
        name: 'Cryptanalyst in Chief Elizebeth Smith Friedman.pptx',
        type: 'pptx',
        rank: '14'
      },
      {
        date: 'Thu Jun 20 08:00:04 2013',
        name: 'Villa.Storrer.bsmt.res.jpg',
        type: 'jpg',
        rank: '15'
      },
      {
        date: 'Mon Feb 11 09:47:26 2013',
        name: 'Villa.before.ext.rest/scan0007.jpg',
        type: 'jpg',
        rank: '16'
      },
      {
        date: 'Wed Feb 16 08:25:26 2005',
        name: 'Villa.before.ext.rest/Exterior Restoration of the Fabyan Villa Museum.doc',
        type: 'doc',
        rank: '17'
      },
      {
        date: 'Thu Sep 21 12:29:46 2023',
        name: 'Villa.before.ext.rest/Thumbs.db',
        type: 'db',
        rank: '18'
      },
      {
        date: 'Wed Jul 18 09:52:56 2007',
        name: 'Villa.before.ext.rest/199601054.jpg',
        type: 'jpg',
        rank: '19'
      },
      {
        date: 'Mon Feb 11 09:48:06 2013',
        name: 'Villa.before.ext.rest/scan0008.jpg',
        type: 'jpg',
        rank: '20'
      },
      {
        date: 'Thu Apr 26 10:03:02 2012',
        name: 'scan0008.jpg',
        type: 'jpg',
        rank: '21'
      },
      {
        date: 'Thu Apr 25 11:35:54 2019',
        name: '20190501_FPDKC Meeting_AGENDA.docx',
        type: 'docx',
        rank: '22'
      },
      {
        date: 'Mon Feb 22 11:38:00 2016',
        name: 'broc.map.label.1.jpg',
        type: 'jpg',
        rank: '23'
      },
      {
        date: 'Mon Jul 25 10:32:50 2005',
        name: 'wm, lyla, kids award 021.jpg',
        type: 'jpg',
        rank: '24'
      },
      {
        date: 'Tue Oct  3 12:06:38 2023',
        name: 'Screenshot 2023-10-03 140638.png',
        type: 'png',
        rank: '25'
      },
      {
        date: 'Mon May 16 19:14:14 2022',
        name: 'Villa Window Earring SVG PNG.png',
        type: 'png',
        rank: '26'
      },
      {
        date: 'Wed Oct  1 11:32:58 2008',
        name: 'windmill.historypage.wpd',
        type: 'wpd',
        rank: '27'
      },
      {
        date: 'Wed Aug 29 09:37:34 2007',
        name: 'wrightwkendpr.doc',
        type: 'doc',
        rank: '28'
      }
    ]
  }

  getProductsData() {
    return [
      {
        id: '1000',
        code: 'f230fh0g3',
        name: 'Bamboo Watch',
        description: 'Product Description',
        image: 'bamboo-watch.jpg',
        price: 65,
        category: 'Accessories',
        quantity: 24,
        inventoryStatus: 'INSTOCK',
        rating: 5
      },
      {
        id: '1001',
        code: 'nvklal433',
        name: 'Black Watch',
        description: 'Product Description',
        image: 'black-watch.jpg',
        price: 72,
        category: 'Accessories',
        quantity: 61,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4
      },
      {
        id: '1002',
        code: 'zz21cz3c1',
        name: 'Blue Band',
        description: 'Product Description',
        image: 'blue-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 2,
        inventoryStatus: 'LOWSTOCK',
        rating: 3
      },
      {
        id: '1003',
        code: '244wgerg2',
        name: 'Blue T-Shirt',
        description: 'Product Description',
        image: 'blue-t-shirt.jpg',
        price: 29,
        category: 'Clothing',
        quantity: 25,
        inventoryStatus: 'INSTOCK',
        rating: 5
      },
      {
        id: '1004',
        code: 'h456wer53',
        name: 'Bracelet',
        description: 'Product Description',
        image: 'bracelet.jpg',
        price: 15,
        category: 'Accessories',
        quantity: 73,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1005',
        code: 'av2231fwg',
        name: 'Brown Purse',
        description: 'Product Description',
        image: 'brown-purse.jpg',
        price: 120,
        category: 'Accessories',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4
      },
      {
        id: '1006',
        code: 'bib36pfvm',
        name: 'Chakra Bracelet',
        description: 'Product Description',
        image: 'chakra-bracelet.jpg',
        price: 32,
        category: 'Accessories',
        quantity: 5,
        inventoryStatus: 'LOWSTOCK',
        rating: 3
      },
      {
        id: '1007',
        code: 'mbvjkgip5',
        name: 'Galaxy Earrings',
        description: 'Product Description',
        image: 'galaxy-earrings.jpg',
        price: 34,
        category: 'Accessories',
        quantity: 23,
        inventoryStatus: 'INSTOCK',
        rating: 5
      },
      {
        id: '1008',
        code: 'vbb124btr',
        name: 'Game Controller',
        description: 'Product Description',
        image: 'game-controller.jpg',
        price: 99,
        category: 'Electronics',
        quantity: 2,
        inventoryStatus: 'LOWSTOCK',
        rating: 4
      },
      {
        id: '1009',
        code: 'cm230f032',
        name: 'Gaming Set',
        description: 'Product Description',
        image: 'gaming-set.jpg',
        price: 299,
        category: 'Electronics',
        quantity: 63,
        inventoryStatus: 'INSTOCK',
        rating: 3
      },
      {
        id: '1010',
        code: 'plb34234v',
        name: 'Gold Phone Case',
        description: 'Product Description',
        image: 'gold-phone-case.jpg',
        price: 24,
        category: 'Accessories',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4
      },
      {
        id: '1011',
        code: '4920nnc2d',
        name: 'Green Earbuds',
        description: 'Product Description',
        image: 'green-earbuds.jpg',
        price: 89,
        category: 'Electronics',
        quantity: 23,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1012',
        code: '250vm23cc',
        name: 'Green T-Shirt',
        description: 'Product Description',
        image: 'green-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 74,
        inventoryStatus: 'INSTOCK',
        rating: 5
      },
      {
        id: '1013',
        code: 'fldsmn31b',
        name: 'Grey T-Shirt',
        description: 'Product Description',
        image: 'grey-t-shirt.jpg',
        price: 48,
        category: 'Clothing',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 3
      },
      {
        id: '1014',
        code: 'waas1x2as',
        name: 'Headphones',
        description: 'Product Description',
        image: 'headphones.jpg',
        price: 175,
        category: 'Electronics',
        quantity: 8,
        inventoryStatus: 'LOWSTOCK',
        rating: 5
      },
      {
        id: '1015',
        code: 'vb34btbg5',
        name: 'Light Green T-Shirt',
        description: 'Product Description',
        image: 'light-green-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 34,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1016',
        code: 'k8l6j58jl',
        name: 'Lime Band',
        description: 'Product Description',
        image: 'lime-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 12,
        inventoryStatus: 'INSTOCK',
        rating: 3
      },
      {
        id: '1017',
        code: 'v435nn85n',
        name: 'Mini Speakers',
        description: 'Product Description',
        image: 'mini-speakers.jpg',
        price: 85,
        category: 'Clothing',
        quantity: 42,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1018',
        code: '09zx9c0zc',
        name: 'Painted Phone Case',
        description: 'Product Description',
        image: 'painted-phone-case.jpg',
        price: 56,
        category: 'Accessories',
        quantity: 41,
        inventoryStatus: 'INSTOCK',
        rating: 5
      },
      {
        id: '1019',
        code: 'mnb5mb2m5',
        name: 'Pink Band',
        description: 'Product Description',
        image: 'pink-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 63,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1020',
        code: 'r23fwf2w3',
        name: 'Pink Purse',
        description: 'Product Description',
        image: 'pink-purse.jpg',
        price: 110,
        category: 'Accessories',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4
      },
      {
        id: '1021',
        code: 'pxpzczo23',
        name: 'Purple Band',
        description: 'Product Description',
        image: 'purple-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 6,
        inventoryStatus: 'LOWSTOCK',
        rating: 3
      },
      {
        id: '1022',
        code: '2c42cb5cb',
        name: 'Purple Gemstone Necklace',
        description: 'Product Description',
        image: 'purple-gemstone-necklace.jpg',
        price: 45,
        category: 'Accessories',
        quantity: 62,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1023',
        code: '5k43kkk23',
        name: 'Purple T-Shirt',
        description: 'Product Description',
        image: 'purple-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 2,
        inventoryStatus: 'LOWSTOCK',
        rating: 5
      },
      {
        id: '1024',
        code: 'lm2tny2k4',
        name: 'Shoes',
        description: 'Product Description',
        image: 'shoes.jpg',
        price: 64,
        category: 'Clothing',
        quantity: 0,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1025',
        code: 'nbm5mv45n',
        name: 'Sneakers',
        description: 'Product Description',
        image: 'sneakers.jpg',
        price: 78,
        category: 'Clothing',
        quantity: 52,
        inventoryStatus: 'INSTOCK',
        rating: 4
      },
      {
        id: '1026',
        code: 'zx23zc42c',
        name: 'Teal T-Shirt',
        description: 'Product Description',
        image: 'teal-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 3,
        inventoryStatus: 'LOWSTOCK',
        rating: 3
      },
      {
        id: '1027',
        code: 'acvx872gc',
        name: 'Yellow Earbuds',
        description: 'Product Description',
        image: 'yellow-earbuds.jpg',
        price: 89,
        category: 'Electronics',
        quantity: 35,
        inventoryStatus: 'INSTOCK',
        rating: 3
      },
      {
        id: '1028',
        code: 'tx125ck42',
        name: 'Yoga Mat',
        description: 'Product Description',
        image: 'yoga-mat.jpg',
        price: 20,
        category: 'Fitness',
        quantity: 15,
        inventoryStatus: 'INSTOCK',
        rating: 5
      },
      {
        id: '1029',
        code: 'gwuby345v',
        name: 'Yoga Set',
        description: 'Product Description',
        image: 'yoga-set.jpg',
        price: 20,
        category: 'Fitness',
        quantity: 25,
        inventoryStatus: 'INSTOCK',
        rating: 8
      }
    ];
  }

  getProductsWithOrdersData() {
    return [
      {
        id: '1000',
        code: 'f230fh0g3',
        name: 'Bamboo Watch',
        description: 'Product Description',
        image: 'bamboo-watch.jpg',
        price: 65,
        category: 'Accessories',
        quantity: 24,
        inventoryStatus: 'INSTOCK',
        rating: 5,
        orders: [
          {
            id: '1000-0',
            productCode: 'f230fh0g3',
            date: '2020-09-13',
            amount: 65,
            quantity: 1,
            customer: 'David James',
            status: 'PENDING'
          },
          {
            id: '1000-1',
            productCode: 'f230fh0g3',
            date: '2020-05-14',
            amount: 130,
            quantity: 2,
            customer: 'Leon Rodrigues',
            status: 'DELIVERED'
          },
          {
            id: '1000-2',
            productCode: 'f230fh0g3',
            date: '2019-01-04',
            amount: 65,
            quantity: 1,
            customer: 'Juan Alejandro',
            status: 'RETURNED'
          },
          {
            id: '1000-3',
            productCode: 'f230fh0g3',
            date: '2020-09-13',
            amount: 195,
            quantity: 3,
            customer: 'Claire Morrow',
            status: 'CANCELLED'
          }
        ]
      },
      {
        id: '1001',
        code: 'nvklal433',
        name: 'Black Watch',
        description: 'Product Description',
        image: 'black-watch.jpg',
        price: 72,
        category: 'Accessories',
        quantity: 61,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1001-0',
            productCode: 'nvklal433',
            date: '2020-05-14',
            amount: 72,
            quantity: 1,
            customer: 'Maisha Jefferson',
            status: 'DELIVERED'
          },
          {
            id: '1001-1',
            productCode: 'nvklal433',
            date: '2020-02-28',
            amount: 144,
            quantity: 2,
            customer: 'Octavia Murillo',
            status: 'PENDING'
          }
        ]
      },
      {
        id: '1002',
        code: 'zz21cz3c1',
        name: 'Blue Band',
        description: 'Product Description',
        image: 'blue-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 2,
        inventoryStatus: 'LOWSTOCK',
        rating: 3,
        orders: [
          {
            id: '1002-0',
            productCode: 'zz21cz3c1',
            date: '2020-07-05',
            amount: 79,
            quantity: 1,
            customer: 'Stacey Leja',
            status: 'DELIVERED'
          },
          {
            id: '1002-1',
            productCode: 'zz21cz3c1',
            date: '2020-02-06',
            amount: 79,
            quantity: 1,
            customer: 'Ashley Wickens',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1003',
        code: '244wgerg2',
        name: 'Blue T-Shirt',
        description: 'Product Description',
        image: 'blue-t-shirt.jpg',
        price: 29,
        category: 'Clothing',
        quantity: 25,
        inventoryStatus: 'INSTOCK',
        rating: 5,
        orders: []
      },
      {
        id: '1004',
        code: 'h456wer53',
        name: 'Bracelet',
        description: 'Product Description',
        image: 'bracelet.jpg',
        price: 15,
        category: 'Accessories',
        quantity: 73,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1004-0',
            productCode: 'h456wer53',
            date: '2020-09-05',
            amount: 60,
            quantity: 4,
            customer: 'Mayumi Misaki',
            status: 'PENDING'
          },
          {
            id: '1004-1',
            productCode: 'h456wer53',
            date: '2019-04-16',
            amount: 2,
            quantity: 30,
            customer: 'Francesco Salvatore',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1005',
        code: 'av2231fwg',
        name: 'Brown Purse',
        description: 'Product Description',
        image: 'brown-purse.jpg',
        price: 120,
        category: 'Accessories',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4,
        orders: [
          {
            id: '1005-0',
            productCode: 'av2231fwg',
            date: '2020-01-25',
            amount: 120,
            quantity: 1,
            customer: 'Isabel Sinclair',
            status: 'RETURNED'
          },
          {
            id: '1005-1',
            productCode: 'av2231fwg',
            date: '2019-03-12',
            amount: 240,
            quantity: 2,
            customer: 'Lionel Clifford',
            status: 'DELIVERED'
          },
          {
            id: '1005-2',
            productCode: 'av2231fwg',
            date: '2019-05-05',
            amount: 120,
            quantity: 1,
            customer: 'Cody Chavez',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1006',
        code: 'bib36pfvm',
        name: 'Chakra Bracelet',
        description: 'Product Description',
        image: 'chakra-bracelet.jpg',
        price: 32,
        category: 'Accessories',
        quantity: 5,
        inventoryStatus: 'LOWSTOCK',
        rating: 3,
        orders: [
          {
            id: '1006-0',
            productCode: 'bib36pfvm',
            date: '2020-02-24',
            amount: 32,
            quantity: 1,
            customer: 'Arvin Darci',
            status: 'DELIVERED'
          },
          {
            id: '1006-1',
            productCode: 'bib36pfvm',
            date: '2020-01-14',
            amount: 64,
            quantity: 2,
            customer: 'Izzy Jones',
            status: 'PENDING'
          }
        ]
      },
      {
        id: '1007',
        code: 'mbvjkgip5',
        name: 'Galaxy Earrings',
        description: 'Product Description',
        image: 'galaxy-earrings.jpg',
        price: 34,
        category: 'Accessories',
        quantity: 23,
        inventoryStatus: 'INSTOCK',
        rating: 5,
        orders: [
          {
            id: '1007-0',
            productCode: 'mbvjkgip5',
            date: '2020-06-19',
            amount: 34,
            quantity: 1,
            customer: 'Jennifer Smith',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1008',
        code: 'vbb124btr',
        name: 'Game Controller',
        description: 'Product Description',
        image: 'game-controller.jpg',
        price: 99,
        category: 'Electronics',
        quantity: 2,
        inventoryStatus: 'LOWSTOCK',
        rating: 4,
        orders: [
          {
            id: '1008-0',
            productCode: 'vbb124btr',
            date: '2020-01-05',
            amount: 99,
            quantity: 1,
            customer: 'Jeanfrancois David',
            status: 'DELIVERED'
          },
          {
            id: '1008-1',
            productCode: 'vbb124btr',
            date: '2020-01-19',
            amount: 198,
            quantity: 2,
            customer: 'Ivar Greenwood',
            status: 'RETURNED'
          }
        ]
      },
      {
        id: '1009',
        code: 'cm230f032',
        name: 'Gaming Set',
        description: 'Product Description',
        image: 'gaming-set.jpg',
        price: 299,
        category: 'Electronics',
        quantity: 63,
        inventoryStatus: 'INSTOCK',
        rating: 3,
        orders: [
          {
            id: '1009-0',
            productCode: 'cm230f032',
            date: '2020-06-24',
            amount: 299,
            quantity: 1,
            customer: 'Kadeem Mujtaba',
            status: 'PENDING'
          },
          {
            id: '1009-1',
            productCode: 'cm230f032',
            date: '2020-05-11',
            amount: 299,
            quantity: 1,
            customer: 'Ashley Wickens',
            status: 'DELIVERED'
          },
          {
            id: '1009-2',
            productCode: 'cm230f032',
            date: '2019-02-07',
            amount: 299,
            quantity: 1,
            customer: 'Julie Johnson',
            status: 'DELIVERED'
          },
          {
            id: '1009-3',
            productCode: 'cm230f032',
            date: '2020-04-26',
            amount: 299,
            quantity: 1,
            customer: 'Tony Costa',
            status: 'CANCELLED'
          }
        ]
      },
      {
        id: '1010',
        code: 'plb34234v',
        name: 'Gold Phone Case',
        description: 'Product Description',
        image: 'gold-phone-case.jpg',
        price: 24,
        category: 'Accessories',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4,
        orders: [
          {
            id: '1010-0',
            productCode: 'plb34234v',
            date: '2020-02-04',
            amount: 24,
            quantity: 1,
            customer: 'James Butt',
            status: 'DELIVERED'
          },
          {
            id: '1010-1',
            productCode: 'plb34234v',
            date: '2020-05-05',
            amount: 48,
            quantity: 2,
            customer: 'Josephine Darakjy',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1011',
        code: '4920nnc2d',
        name: 'Green Earbuds',
        description: 'Product Description',
        image: 'green-earbuds.jpg',
        price: 89,
        category: 'Electronics',
        quantity: 23,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1011-0',
            productCode: '4920nnc2d',
            date: '2020-06-01',
            amount: 89,
            quantity: 1,
            customer: 'Art Venere',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1012',
        code: '250vm23cc',
        name: 'Green T-Shirt',
        description: 'Product Description',
        image: 'green-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 74,
        inventoryStatus: 'INSTOCK',
        rating: 5,
        orders: [
          {
            id: '1012-0',
            productCode: '250vm23cc',
            date: '2020-02-05',
            amount: 49,
            quantity: 1,
            customer: 'Lenna Paprocki',
            status: 'DELIVERED'
          },
          {
            id: '1012-1',
            productCode: '250vm23cc',
            date: '2020-02-15',
            amount: 49,
            quantity: 1,
            customer: 'Donette Foller',
            status: 'PENDING'
          }
        ]
      },
      {
        id: '1013',
        code: 'fldsmn31b',
        name: 'Grey T-Shirt',
        description: 'Product Description',
        image: 'grey-t-shirt.jpg',
        price: 48,
        category: 'Clothing',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 3,
        orders: [
          {
            id: '1013-0',
            productCode: 'fldsmn31b',
            date: '2020-04-01',
            amount: 48,
            quantity: 1,
            customer: 'Simona Morasca',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1014',
        code: 'waas1x2as',
        name: 'Headphones',
        description: 'Product Description',
        image: 'headphones.jpg',
        price: 175,
        category: 'Electronics',
        quantity: 8,
        inventoryStatus: 'LOWSTOCK',
        rating: 5,
        orders: [
          {
            id: '1014-0',
            productCode: 'waas1x2as',
            date: '2020-05-15',
            amount: 175,
            quantity: 1,
            customer: 'Lenna Paprocki',
            status: 'DELIVERED'
          },
          {
            id: '1014-1',
            productCode: 'waas1x2as',
            date: '2020-01-02',
            amount: 175,
            quantity: 1,
            customer: 'Donette Foller',
            status: 'CANCELLED'
          }
        ]
      },
      {
        id: '1015',
        code: 'vb34btbg5',
        name: 'Light Green T-Shirt',
        description: 'Product Description',
        image: 'light-green-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 34,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1015-0',
            productCode: 'vb34btbg5',
            date: '2020-07-02',
            amount: 98,
            quantity: 2,
            customer: 'Mitsue Tollner',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1016',
        code: 'k8l6j58jl',
        name: 'Lime Band',
        description: 'Product Description',
        image: 'lime-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 12,
        inventoryStatus: 'INSTOCK',
        rating: 3,
        orders: []
      },
      {
        id: '1017',
        code: 'v435nn85n',
        name: 'Mini Speakers',
        description: 'Product Description',
        image: 'mini-speakers.jpg',
        price: 85,
        category: 'Clothing',
        quantity: 42,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1017-0',
            productCode: 'v435nn85n',
            date: '2020-07-12',
            amount: 85,
            quantity: 1,
            customer: 'Minna Amigon',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1018',
        code: '09zx9c0zc',
        name: 'Painted Phone Case',
        description: 'Product Description',
        image: 'painted-phone-case.jpg',
        price: 56,
        category: 'Accessories',
        quantity: 41,
        inventoryStatus: 'INSTOCK',
        rating: 5,
        orders: [
          {
            id: '1018-0',
            productCode: '09zx9c0zc',
            date: '2020-07-01',
            amount: 56,
            quantity: 1,
            customer: 'Abel Maclead',
            status: 'DELIVERED'
          },
          {
            id: '1018-1',
            productCode: '09zx9c0zc',
            date: '2020-05-02',
            amount: 56,
            quantity: 1,
            customer: 'Minna Amigon',
            status: 'RETURNED'
          }
        ]
      },
      {
        id: '1019',
        code: 'mnb5mb2m5',
        name: 'Pink Band',
        description: 'Product Description',
        image: 'pink-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 63,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: []
      },
      {
        id: '1020',
        code: 'r23fwf2w3',
        name: 'Pink Purse',
        description: 'Product Description',
        image: 'pink-purse.jpg',
        price: 110,
        category: 'Accessories',
        quantity: 0,
        inventoryStatus: 'OUTOFSTOCK',
        rating: 4,
        orders: [
          {
            id: '1020-0',
            productCode: 'r23fwf2w3',
            date: '2020-05-29',
            amount: 110,
            quantity: 1,
            customer: 'Kiley Caldarera',
            status: 'DELIVERED'
          },
          {
            id: '1020-1',
            productCode: 'r23fwf2w3',
            date: '2020-02-11',
            amount: 220,
            quantity: 2,
            customer: 'Graciela Ruta',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1021',
        code: 'pxpzczo23',
        name: 'Purple Band',
        description: 'Product Description',
        image: 'purple-band.jpg',
        price: 79,
        category: 'Fitness',
        quantity: 6,
        inventoryStatus: 'LOWSTOCK',
        rating: 3,
        orders: [
          {
            id: '1021-0',
            productCode: 'pxpzczo23',
            date: '2020-02-02',
            amount: 79,
            quantity: 1,
            customer: 'Cammy Albares',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1022',
        code: '2c42cb5cb',
        name: 'Purple Gemstone Necklace',
        description: 'Product Description',
        image: 'purple-gemstone-necklace.jpg',
        price: 45,
        category: 'Accessories',
        quantity: 62,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1022-0',
            productCode: '2c42cb5cb',
            date: '2020-06-29',
            amount: 45,
            quantity: 1,
            customer: 'Mattie Poquette',
            status: 'DELIVERED'
          },
          {
            id: '1022-1',
            productCode: '2c42cb5cb',
            date: '2020-02-11',
            amount: 135,
            quantity: 3,
            customer: 'Meaghan Garufi',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1023',
        code: '5k43kkk23',
        name: 'Purple T-Shirt',
        description: 'Product Description',
        image: 'purple-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 2,
        inventoryStatus: 'LOWSTOCK',
        rating: 5,
        orders: [
          {
            id: '1023-0',
            productCode: '5k43kkk23',
            date: '2020-04-15',
            amount: 49,
            quantity: 1,
            customer: 'Gladys Rim',
            status: 'RETURNED'
          }
        ]
      },
      {
        id: '1024',
        code: 'lm2tny2k4',
        name: 'Shoes',
        description: 'Product Description',
        image: 'shoes.jpg',
        price: 64,
        category: 'Clothing',
        quantity: 0,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: []
      },
      {
        id: '1025',
        code: 'nbm5mv45n',
        name: 'Sneakers',
        description: 'Product Description',
        image: 'sneakers.jpg',
        price: 78,
        category: 'Clothing',
        quantity: 52,
        inventoryStatus: 'INSTOCK',
        rating: 4,
        orders: [
          {
            id: '1025-0',
            productCode: 'nbm5mv45n',
            date: '2020-02-19',
            amount: 78,
            quantity: 1,
            customer: 'Yuki Whobrey',
            status: 'DELIVERED'
          },
          {
            id: '1025-1',
            productCode: 'nbm5mv45n',
            date: '2020-05-21',
            amount: 78,
            quantity: 1,
            customer: 'Fletcher Flosi',
            status: 'PENDING'
          }
        ]
      },
      {
        id: '1026',
        code: 'zx23zc42c',
        name: 'Teal T-Shirt',
        description: 'Product Description',
        image: 'teal-t-shirt.jpg',
        price: 49,
        category: 'Clothing',
        quantity: 3,
        inventoryStatus: 'LOWSTOCK',
        rating: 3,
        orders: [
          {
            id: '1026-0',
            productCode: 'zx23zc42c',
            date: '2020-04-24',
            amount: 98,
            quantity: 2,
            customer: 'Bette Nicka',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1027',
        code: 'acvx872gc',
        name: 'Yellow Earbuds',
        description: 'Product Description',
        image: 'yellow-earbuds.jpg',
        price: 89,
        category: 'Electronics',
        quantity: 35,
        inventoryStatus: 'INSTOCK',
        rating: 3,
        orders: [
          {
            id: '1027-0',
            productCode: 'acvx872gc',
            date: '2020-01-29',
            amount: 89,
            quantity: 1,
            customer: 'Veronika Inouye',
            status: 'DELIVERED'
          },
          {
            id: '1027-1',
            productCode: 'acvx872gc',
            date: '2020-06-11',
            amount: 89,
            quantity: 1,
            customer: 'Willard Kolmetz',
            status: 'DELIVERED'
          }
        ]
      },
      {
        id: '1028',
        code: 'tx125ck42',
        name: 'Yoga Mat',
        description: 'Product Description',
        image: 'yoga-mat.jpg',
        price: 20,
        category: 'Fitness',
        quantity: 15,
        inventoryStatus: 'INSTOCK',
        rating: 5,
        orders: []
      },
      {
        id: '1029',
        code: 'gwuby345v',
        name: 'Yoga Set',
        description: 'Product Description',
        image: 'yoga-set.jpg',
        price: 20,
        category: 'Fitness',
        quantity: 25,
        inventoryStatus: 'INSTOCK',
        rating: 8,
        orders: [
          {
            id: '1029-0',
            productCode: 'gwuby345v',
            date: '2020-02-14',
            amount: 4,
            quantity: 80,
            customer: 'Maryann Royster',
            status: 'DELIVERED'
          }
        ]
      }
    ];
  }
}
