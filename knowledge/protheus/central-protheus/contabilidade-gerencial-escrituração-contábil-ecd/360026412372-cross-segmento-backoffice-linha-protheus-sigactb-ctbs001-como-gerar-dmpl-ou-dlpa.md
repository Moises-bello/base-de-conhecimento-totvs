---
article_id: 360026412372
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 79b3705a4e7de8c4f64ead9727f062a0bba12cc7299f5ff45abf304281edf546
fetched_at: '2026-06-28T22:40:44.538604+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Como gerar
  DMPL  ou DLPA na ECD? (Registros J210 e J215)
type: support-article
updated_at: '2024-05-17T12:05:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026412372-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Como-gerar-DMPL-ou-DLPA-na-ECD-Registros-J210-e-J215
---

**Dúvida**

Como gerar a DMPL ou DPLA (Registros J210 e J215) na arquivo da ECD a partir do layout 7?

**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão P12   
  
**Solução**

Para configuração do DMPL/DLPA para geração da ECD no Protheus siga os passos:

1) [Rotina CTBA161 (visão gerencial)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search) Criar apenas uma entidade analítica contendo o range das contas Patrimoniais, essa entidade corresponderá ao registro J210 no arquivo txt.

* Emita o relatório [CTBR530](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012434852?source=search) - e veja se o saldo apresentado está correto

![](https://totvssuporte.zendesk.com/attachments/token/DmrI1AmyF3CgzsblSvuGCP4O7/?name=inline942684415.png)  
  
2) Rotina CTBA130 (configuração de livro) criar um livro relacionando a visão gerencial  
  
![](https://totvssuporte.zendesk.com/attachments/token/WiTE1goWyNDR2tm8LZvjOJuO9/?name=inline-1210890097.png)​  
​  
  
3) Na rotina CTBS001 Wizard da ECD informar os campos referente ao DMPL ou DPLA:  
  
![](https://totvssuporte.zendesk.com/attachments/token/Ey9WkhNipSs5CL0vIpC4DqES2/?name=inline1963913973.png)

J200: Histórico Fato Contábil - cadastrar? - parâmetro bloqueado conforme documentação : [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025580492-MP-SIGACTB-ECD-LEIAUTE-7-J200-HIST%C3%93RICO-FATO-CONTABIL-DESABILITADO?source=search)

4) Assinale SIM para o registro J215.

obs: Ao informar o J210, o registro J215 é necessário para composição correta do demonstrativo.

![](https://totvssuporte.zendesk.com/attachments/token/DzS7YRHD0O7WkKDCmg9WhJsq9/?name=inline-464738045.png)

Ao clicar em "Avançar" sistema apresenta a tela abaixo , clique em "Finalizar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026001432)

Clique em "Avançar "

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026003991)

Clique em "Finalizar "

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026001472)

Será apresentada a opção para cadastrar o "Detalhe Fato Contábil"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026004191)

* Preencha os campos abaixo

 CSO\_CODAGL - deve clicar a Lupa selecionar codigo de aglutinação apresentado , que se trata da visão gerencial de DMPL informada na geração da visão

CSO\_INDFAT - verifique através do manual da receita a informação que deve ser informada

CSO\_CODFAT -Informe o COD do fato contábil (deve ser informado o Código do fato contábil )

CSO\_DESFAT - Informe a descrição do fato contábil

![](https://totvssuporte.zendesk.com/attachments/token/vRnlhZX4A01wHE48gRysg0cUC/?name=inline-135607800.png)

5) Deverá ser feito o detalhamento das movimentações do PL.

![](https://totvssuporte.zendesk.com/attachments/token/NxpdcdAhTRxzs6eV1zKn7n61V/?name=inline-363345810.png)

6) No arquivo TXT:  
  
![](https://totvssuporte.zendesk.com/attachments/token/JsLbBWL2vnSPKl68X0VDzO1Oz/?name=inline761101544.png)  
  
  
Ao exportar no validador:​​  
  
![](https://totvssuporte.zendesk.com/attachments/token/b2LwHhAc8uTydPYSxBYyeIcCA/?name=inline1322197660.png)​  
  
  
Visualizações + DMPL (PGE)  
Note que o Saldo Anterior e o Saldo final o PGE faz o mapeamento conforme o saldo do J210.  
  
|J210|1|00200000000000000007008|DMPL|60,00|C|10860,00|C||  
|J215|001|Acréscimo de capital|1000,00|C|  
|J215|002|Ajustes realizados em exercícios passados|800,00|C|  
|J215|003|Resultado líquido do exercício|9000,00|C|  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/KbFix7V85tmcJqZGON1W8R6MC/?name=inline-892710046.png)

Facilitador de detalhamento:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018715631-MP-SIGACTB-ECD-Facilitador-ECD-DMPL-Recupere-os-registros-J200-e-J215-de-uma-revis%C3%A3o-anterior>

Veja mais:

[MP-SIGACTB ECD J215 DESC\_FAT CAMPO OBRIGATORIO NAO PREENCHIDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025126732-MP-SIGACTB-ECD-J215-DESC-FAT-CAMPO-OBRIGATORIO-NAO-PREENCHIDO?source=search)

[MP - SIGACTB: Facilitador ECD/ DMPL. Recupere os registros J200 e J215 de uma revisão anterior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018715631-MP-SIGACTB-Facilitador-ECD-DMPL-Recupere-os-registros-J200-e-J215-de-uma-revis%C3%A3o-anterior?source=search)

[MP - SIGACTB: Como efetuar o detalhamento do Fato contábil e do histórico do fato contábil?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018428472-MP-SIGACTB-Como-efetuar-o-detalhamento-do-Fato-cont%C3%A1bil-e-do-hist%C3%B3rico-do-fato-cont%C3%A1bil-?source=search)

[MP-SIGACTB ECD : J800 LAYOUT 7 COMO GERAR NOTA EXPLICATIVA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025129432-MP-SIGACTB-ECD-J800-LAYOUT-7-COMO-GERAR-NOTA-EXPLICATIVA?source=search)

[MP - SIGACTB: ECD LAYOUT 2 AO 6 : COMO GERAR OS REGISTROS J200 J210 J215](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018428472/preview/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzYwMDE4NDI4NDcyLCJleHAiOjE1NTQ5MjAwNDR9.7d9dxydoP3X1saeAlB95V-3HlTx8MD-Rd7H385ZXc-I)

[ECD0044\_Fato Contábil - MV\_ECDTRIA , para que seja gerado o J215 para o período anual](https://tdn.totvs.com/pages/releaseview.action?pageId=773517445)

Para exibição das contas com saldos zerados no registro J210, ativar o parâmetro [MV\_CTBSLDZ](https://tdn.totvs.com/pages/viewpage.action?pageId=621605812)
