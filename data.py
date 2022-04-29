insert_everything = """
INSERT INTO usuario VALUES
(0,'TajLubaydAntoun@armyspy.com','eeCh9lu4','Taylor','21 Lincoln Green Lane'),
(1,'ShanTing@jourrapide.com','eLoojae2','Shan','Ziegelgasse 44'),
(2,'TaylorFrost@cuvox.de','AeS4pieYoh','Taj','Kálmán Imre u. 48.'),
(3,'EvaOlsen@superrito.com','kae8Oox6pee','Eva','Infanterivegen 202'),
(4,'ViljoHietamies@dayrep.com','eeCh9lu4','Viljo','Schachterlweg 46'),
(5,'Zumoritotofu@cuvox.de','Bo7Aithooqu','Zumoritotofu','Breitenstrasse 45'),
(6,'EllaLofgren@jourrapide.com','jaiPhoo5jah','Ella','Pesolantie 58'),
(7,'MethZanis@cuvox.de','noo3ahK4ibu1','Meth','8 Bury Rd'),
(8,'LarisaPokrovskaya@dayrep.com','daph8AhV4Se','Larisa','Castelao 99'),
(9,'BalighHamdanRahal@gustr.com','Mohwae2oh','Baligh','C/ Andalucía 20'),
(10,'KirstiHaapaniemi@superrito.com','PaecaiT4zoh','Kirsti','P.O. Box 286');

INSERT INTO cliente VALUES
('(55) 45 719598119','6665',0),
('(73) 61 192734440','3395',1),
('(56) 82 775887381',NULL,2),
('(19) 17 211414055','9813',3),
(NULL,'8525',4),
('(32) 37 690625518','4459',5);

INSERT INTO vendedor VALUES
('Auto Works'	,'(12) 55 767366898','4929125251095654',0.05,03548944356,6),
('Polk Brothers','(57) 61 599651191','4485685700162930',0.05,33249088173,7),
('Complete Tech','(83) 74 595168507','4929793255577959',0.05,36055188042879,8),
('Your Library'	,'(15) 32 657389423','9846165198845618',0.08,63013001388764,9);

INSERT INTO individual VALUES
(0.01,6),
(0.02,7);

INSERT INTO profissional VALUES
(0.09,8),
(0.05,9);

INSERT INTO entregador VALUES
('Taylor delivery','(55) 45 719598119',78965415963,0),
('Correios','(55) 51 456892143',54789658213547,10),
('FEDEX','(73) 61 192734440',59423681547982,1);

INSERT INTO moderador VALUES
('(56) 82 775887381',56821463985,2),
('(55) 51 957382446',48962531574,4);

INSERT INTO marca VALUES
('Apple'),
('Samsung'),
('Sony'),
('Dell'),
('Pearson'),
('Intrinseca'),
('Coca-cola'),
('Lacta');

INSERT INTO categoria VALUES
('Computadores'),
('Televisores'),
('Celulares'),
('Livros'),
('Alimentos');

INSERT INTO produto VALUES
('Ótimo televisor para você e toda sua família',2599.99,'TV',0,50,8,'Samsung','Televisores'),
('Alto desempenho pra trabalhar e jogar',5999.59,'Notebook',1,30,8,'Dell','Computadores'),
('Perfeito para estudar',2999.59,'Computador de mesa',2,80,8,'Dell','Computadores'),
('Uma nova maneira de assistir',9999.59,'TV',3,80,8,'Sony','Televisores'),
('Seu novo dispositivo preferido',13999.59,'Iphone',4,60,8,'Apple','Celulares'),
('Acompanhe o personagem nessa jornada',29.99,'Harry Potter',5,200,9,'Intrinseca','Livros'),
('Se surpreenda com essa história',19.99,'Percy Jackson',6,250,9,'Pearson','Livros'),
('Edição raríssima, não perca',99.99,'Dom Casmurro',7,1,9,NULL,'Livros'),
('Seu refri favorito, em uma nova embalagem',5.99,'Coca-cola',8,1000,7,'Coca-cola','Alimentos'),
('Autêntico sabor brasileiro, com a qualidade que você conhece',5.49,'Fanta Guaraná',9,900,7,'Coca-cola','Alimentos'),
('O melhor chocolate do mundo',3.49,'Barra Meio Amargo',10,2000,7,'Lacta','Alimentos'),
('Artesanal especial para você',6.49,'Trufa',11,20,7,NULL,'Alimentos'),
('Feitos para você aproveitar',20.49,'Talheres',12,30,7,NULL,NULL),
('Seu novo celular deve ser esse',1499.49,'Celular',13,200,6,'Samsung','Celulares'),
('Performance e desempenho para você',2499.49,'Celular',14,300,6,'Apple','Celulares'),
('Opção de entrada, aproveite o preço',799.49,'Celular',15,500,6,'Samsung','Celulares');

INSERT INTO propriedades VALUES
(0,'4K'),
(0,'40 Polegadas'),
(1,'8GB RAM'),
(1,'Placa de Vídeo Intel HD Graphics'),
(2,'RAM de 4 GB'),
(2,'Tela HD'),
(2,'Bivolt'),
(3,'Resolução Full HD'),
(3,'Tela de 50 polegadas'),
(4,'Versão 13'),
(5,'300 páginas'),
(6,'Número de páginas: 250'),
(7,'Raríssimo'),
(7,'500 páginas');

INSERT INTO oferta VALUES
(0.20,'Nova oferta em celulares selecionados','2022-07-07 00:00','2022-08-08 00:00',0),
(0.05,'Todos os chocolates em promoção!','2022-02-10 00:00','2022-02-10 23:59',1);

INSERT INTO Oferta_Produto VALUES
(4,0),
(13,0),
(15,0),
(10,1),
(11,1);

INSERT INTO Avaliacao VALUES
(6,5,2),
(6,4,4),
(6,4.9,3),
(5,4,3),
(5,4.2,5),
(14,2.1,1),
(15,3.2,1);

INSERT INTO carrinho VALUES
(3,1,1),
(2,13,1),
(6,2,5),
(4,6,5);

INSERT INTO acessa VALUES
(3,'2022-04-04 14:23','2022-04-04 14:24',1),
(2,'2022-04-04 14:26','2022-04-04 14:29',1),
(6,'2022-04-05 9:59','2022-04-05 10:01',5),
(4,'2022-04-05 10:10','2022-04-05 10:15',5),
(10,'2022-03-31 21:15','2022-03-31 22:17',3),
(12,'2022-03-31 22:17','2022-03-31 22:18',2),
(1,'2022-01-09 06:30','2022-01-09 06:31',4),
(2,'2022-01-09 06:32','2022-01-09 06:35',4),
(11,'2022-02-10 07:52','2022-02-10 07:55',1),
(9,'2021-12-25 02:40','2021-12-25 02:41',2),
(15,'2022-02-15 17:00','2022-02-15 17:55',3);

INSERT INTO compra VALUES
(TRUE,'2021-12-25 02:42',5.19,2,9,1,0),
(TRUE,'2022-01-09 06:40',11999.18,4,1,2,1),
(TRUE,'2022-01-09 06:40',8998.77,4,15,3,2),
(TRUE,'2022-02-10 07:59',18.36,1,11,3,3),
(TRUE,'2022-02-15 17:55',799.99,3,15,1,4),
(FALSE,'2022-04-04 14:30',9999.59,1,3,1,5),
(FALSE,'2022-04-04 14:30',2999.59,1,2,1,6);

INSERT INTO local VALUES
('Ziegelgasse 44','Casa Cliente',0,'Destino final'),
('Kálmán Imre u. 48.','Casa Cliente',1,'Destino final'),
('Infanterivegen 202','Casa Cliente',2,'Destino final'),
('Schachterlweg 46','Casa Cliente',3,'Destino final'),
('Curitiba - PR Rua Presidente Vargas 001','Centro de distriubição 01',4,'Intermediário'),
('São Paulo - SP Rua Dom Pedro I 123','Centro de distriubição 02',5,'Intermediário');

INSERT INTO entrega VALUES
(0,4,1),
(0,1,1),
(1,4,1),
(1,3,1),
(2,5,10),
(2,3,10),
(3,0,0),
(4,5,10),
(4,2,10);

INSERT INTO mensagem VALUES
(7, 2, 4, true,'Boa tarde, gostaria de tirar uma dúvida', '2021-12-25 02:30', false, NULL, NULL),
(7, 2, 4, false,'O que seria?', '2021-12-25 02:31', false, NULL, NULL),
(7, 2, 4, true,'Vocês teriam algum refrigerante sabor guaraná?', '2021-12-25 02:32', false, NULL, NULL),
(7, 2, 4, false,'Sim, temos Fanta Guaraná', '2021-12-25 02:33', false, NULL, NULL),
(7, 2, 4, true,'Ótimo, obrigado', '2021-12-25 02:34', false, NULL, NULL),
(8, 4, 2, true, 'Existe algum PC boa nessa loja?', '2022-01-09 06:00', false, NULL, NULL),
(8, 4, 2, false, 'Trabalhamos apenas com produtos de qualidade, senhor', '2022-01-09 06:01', false, NULL, NULL),
(8, 4, 2, true, 'Não é o que parece, só vejo computadores ruins. Vocês não trabalham direito.', '2022-01-09 06:02', true, true, 'Denúncia feita com razão, cliente agiu de forma desrespeitosa. Será notificado para mudar o comportamento'),
(8, 4, 2, false, 'Senhor, pedimos calma', '2022-01-09 06:03', true, false, 'Denúncia infundada. Vendedor agiu de forma cordial.');
"""