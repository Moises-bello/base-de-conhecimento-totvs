---
article_id: 1500010507681
category: Anuais
content_hash: cbe979331796b9ebfe56a5b5df15ddaa251ef588b2b7cb795ae7ff169979a49c
fetched_at: '2026-06-28T22:46:51.121807+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Projetar Aviso Prévio Indenizado na Data de Desligamento'
type: support-article
updated_at: '2025-03-14T10:01:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010507681-RH-RM-FOP-RAIS-Projetar-Aviso-Pr%C3%A9vio-Indenizado-na-Data-de-Desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:07:45 min  
  
Dúvida**Como fazer para considerar a projeção dos dias de aviso prévio indenizado na data de desligamento da RAIS?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.32  
  
**Solução**Para gerar o arquivo da RAIS ano-base 2021 considerando como data de desligamento a do último dia da projeção do aviso prévio indenizado, é necessário acessar o menu **Anuais | RAIS**:  
  
![](https://tdn.totvs.com/download/attachments/223159548/80.png?version=1&modificationDate=1489500071000&api=v2)  
  
Ao abrir rotina, será visualizado o parâmetro **Projeta Aviso Prévio Indenizado na Data de Desligamento**.  
  
O usuário deve marcar este parâmetro, informar qual tipo de arquivo que deseja gerar (RAIS Genérica ou RAIS Retificadora) e os demais campos necessário para a geração da RAIS:  
  
![](https://tdn.totvs.com/download/attachments/223159548/image2018-1-23_7-42-34.png?version=1&modificationDate=1516704156000&api=v2)  
  
Marcando o parâmetro **Projeta Aviso Prévio Indenizado na Data Desligamento**, o processo irá fazer a projeção da data de desligamento somando os dias de aviso indenizado e caso a soma ultrapasse a data de 31/12/2021, não serão preenchidos os campos referente a "Data de Desligamento", Código do tipo de desligamento e verbas rescisórias no arquivo da RAIS. Importante ressaltar que a data deste exemplo considera a RAIS 2022 ano-base 2021.  
  
Sobre o parâmetro **Limitar data projetada para janeiro do ano seguinte**, marcar essa opção para casos de demissão no ano anterior ao ano-base e que a projeção de dias de aviso prévio somado à essa data ultrapassa o mês de janeiro do ano base, evitando assim erro no validador da RAIS que entende que o funcionário deveria ter remuneração no ano base.  
  
**Atenção:**- Os valores das verbas rescisórias não serão levados devido ao validador GDRAIS acusar erro pela falta de data de desligamento quando as verbas são informadas.  
- Os valores que não corresponderem a verbas rescisórias mas estiverem no movimento da rescisão serão levados normalmente. Exemplo: Dias trabalhados, horas extras, faltas, comissões, etc.  
  
Exemplo de quando o parâmetro estiver marcado:  
  
Funcionário demitido em 01/12/2017 e com 50 dias de aviso prévio indenizado:  
  
![](https://tdn.totvs.com/download/attachments/223159548/image2018-1-23_7-45-45.png?version=1&modificationDate=1516704348000&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/223159548/image2018-1-23_7-47-2.png?version=1&modificationDate=1516704424000&api=v2)  
  
No envelope de pagamento do funcionário com as verbas rescisórias, havia os eventos de movimento mensal destacados abaixo:   
  
![](https://tdn.totvs.com/download/attachments/223159548/image2018-1-23_8-3-38.png?version=1&modificationDate=1516705421000&api=v2)  
  
Ao gerar a RAIS ano-base 2017, a data de demissão deste funcionário será projetada para 19/01/2018.   
Com isso, nas informações **Desligamento | Movimentação | Aposentadoria** do GDRAIS, os campos não serão preenchidos:  
  
![](https://tdn.totvs.com/download/attachments/223159548/86.png?version=1&modificationDate=1489509519000&api=v2)  
  
Em **Remuneração Mensal**, o campo referente ao mês em que o funcionário teve a demissão processada e pagamentos de eventos que são de movimentação mensal, foi preenchido com a soma dos eventos de movimento e a quantidade de horas extras:   
  
![](https://tdn.totvs.com/download/attachments/223159548/87.png?version=1&modificationDate=1489509642000&api=v2)  
  
Caso na projeção dos dias de aviso a data for menor ou igual a 31/12/2017, todos os campos serão levados normalmente.   
  
![](https://tdn.totvs.com/download/attachments/223159548/image2018-1-23_8-5-53.png?version=1&modificationDate=1516705555000&api=v2)

![](https://tdn.totvs.com/download/attachments/223159548/image2018-1-23_8-7-26.png?version=1&modificationDate=1516705648000&api=v2)  
  
Ao gerar a RAIS ano-base 2017, a data de demissão deste funcionário será projetada para 31/12/2017.   
Nas informações **Desligamento | Movimentação | Aposentadoria** do GDRAIS, os campos serão preenchidos normalmente.   
  
![](https://tdn.totvs.com/download/attachments/223159548/79.png?version=2&modificationDate=1489510346000&api=v2)  
  
Caso o usuário queira gerar o Arquivo da RAIS ano-base 2017 sem fazer a projeção do aviso prévio indenizado na data de desligamento, basta deixar o parâmetro **Projeta Aviso Prévio Indenizado na Data de Desligamento** desmarcado. O processo irá gerar o arquivo considerando a data de desligamento cadastrada para o funcionário e as verbas rescisórias. Caso a data de desligamento seja projetada para 2018 e o funcionário tenha rescisão complementar em 2018, os valores da rescisão complementar também não serão considerados para a RAIS ano-base 2017. Parar os funcionários que tiveram a data de desligamento projetada para 2018, a data de desligamento e verbas rescisórias serão levados na geração da RAIS ano-base 2017.  
  
**Importante**  
Conforme manual da RAIS ano-base 2014, foram apresentadas novidades quanto a data de desligamento do empregado:  
  
*"VI - A data de desligamento deve ser a data de saída constante na carteira de trabalho (CTPS), que deve corresponder a data do término do aviso prévio, ainda que indenizado."*Em relação a data de desligamento, pairaram algumas dúvidas relativas ao preenchimento correto deste campo, face a interpretação advinda do Manual da RAIS. Assim, o Ministério do Trabalho e Emprego (MTE) foi acionado para solicitarmos orientações quanto ao correto tratamento envolvido à declaração constante como 'Data Desligamento'.  
A TOTVS recepcionou tais esclarecimentos do Ministério do Trabalho e Emprego (MTE) em 12/03/2015, conforme transcrevemos abaixo:  
  
A data de desligamento que deve ser informada na RAIS é a data constante na Instrução Normativa Secretário de Relações do Trabalho – SRT Nº 15 de 14/07/2010 – na pagina relativa ao contrato de trabalho, a do último dia da data projetada para o aviso prévio indenizado.  
  
Face a tal esclarecimento e novas interpretações, implementamos o parâmetro **Projeta Aviso Prévio Indenizado na Data de Desligamento**para atender a Instrução Normativa acima.  
  
Recomendamos aos nossos clientes a revisão desta interpretação conjuntamente com os responsáveis na Empresa pela declaração da RAIS perante ao MTE. É importante que seja analisado e definido qual opção a Empresa fará (data da demissão ou data projetada), a TOTVS implementou no sistema o novo entendimento sem a remoção do anteriormente praticado.

***Informações gerais sobre a RAIS 2022*** *Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
