---
article_id: 13480369069079
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 962e25827f7af43f75588fc6661b4df20a26a462fc27af17600413a41100caf3
fetched_at: '2026-06-28T22:40:52.753608+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD O bloco
  J não foi importado pois contém erros
type: support-article
updated_at: '2023-05-18T18:37:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13480369069079-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-O-bloco-J-n%C3%A3o-foi-importado-pois-cont%C3%A9m-erros
---

**Dúvida**

O bloco J não foi importado pois contém erros   
Registro obrigatório não encontrado J930

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13465781548055)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS  Contabilidade gerencial  - Todas as versões

**Causa**

Como o **validador não especifica exatamente** o erro no Bloco J , se faz **necessário analisar o arquivo** utilizando como base o **manual da receita**

**Caso em sua analise não consiga detectar o que esta incorreto no bloco J , será necessário contatar a Receita , pois o validador não esta especificando o que esta errado no registro**

O erro "O bloco J não foi importado pois contém erros" pode ser apresentado por diversos fatores , neste caso detectamos erro na configuração do J100 , como podemos ver abaixo .

O erro "Registro obrigatório não encontrado J930 " identificamos que o registro não foi gerado

**Solução**

Analisando o arquivo veja  que o campo 06 , na entidade de Passivo estão com A =Ativo , necessário que esteja como  P =Passivo   
   
![](https://totvssuporte.zendesk.com/attachments/token/heZ1Wvso20K4t36W8QHkHoLP9/?name=image.png)  
   
veja no manual  
   
![](https://totvssuporte.zendesk.com/attachments/token/ZKYeFE7IXsxj3oMIA9in2sFpp/?name=image.png)  
   
Para corrigir isso , informe a coluna 2 na configuração da visão gerencial  da entidades do Passivo   
 Para mais detalhes veja : [Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD Registro J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Registro-J100?source=search)  
   
![](https://totvssuporte.zendesk.com/attachments/token/jtakyS4btRyqk2gU6Qwd3ZoKJ/?name=image.png)

* o erro "Registro obrigatório não encontrado J930 " identificamos que o registro não foi gerado

Segue abaixo o procedimento para gerar o registro , como o validador não especifica o erro e o J930 é um registro obrigatório .  
   
  
   
![](https://totvssuporte.zendesk.com/attachments/token/2JmTmxjwHCffn5xvYKuReKeVu/?name=image.png)

* Veja como gerar o J930

[Cross Segmento - Backoffice Linha Protheus -SIGACTB - ECD e ECF - CTBA015 REGISTRO J930 e 0930: Identificação dos Signatários da Escrituração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020083171-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-e-ECF-CTBA015-REGISTRO-J930-e-0930-Identifica%C3%A7%C3%A3o-dos-Signat%C3%A1rios-da-Escritura%C3%A7%C3%A3o?source=search)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD J932 REGISTRO OBRIGATÓRIO NÃO ENCONTRADO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025376331-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J932-REGISTRO-OBRIGAT%C3%93RIO-N%C3%83O-ENCONTRADO?source=search)  
[Cross Segmento - Backoffice Linha Protheus -SIGACTB - ECD - J930 CADASTRO REPRESENTANTE LEGAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006984451-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J930-CADASTRO-REPRESENTANTE-LEGAL-?source=search)
