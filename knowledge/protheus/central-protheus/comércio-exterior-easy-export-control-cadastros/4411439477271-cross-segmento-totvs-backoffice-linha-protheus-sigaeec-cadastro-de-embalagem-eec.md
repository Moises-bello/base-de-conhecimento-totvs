---
article_id: 4411439477271
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 95d005f3db9b74a408ba89dbc0b34b591064e963a3f32bcb2971ffd1a901af84
fetched_at: '2026-06-28T22:36:57.328549+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Cadastro de embalagem
  (EECAT170)
type: support-article
updated_at: '2021-10-25T15:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411439477271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Cadastro-de-embalagem-EECAT170
---

**Dúvida**Como cadastrar embalagem rotina EECAT170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.   
  
**Solução**Neste cadastro deverão ser registradas as embalagens utilizadas nos produtos, desde a embalagem principal do produto até o acondicionamento das cargas. Este cadastro permite informar, em uma pequena manutenção, quantas desta embalagem são “embaladas” por outra, sendo todas elas consideradas no processo para efeito de apuração do peso.   
Abaixo exemplificaremos o comportamento do sistema com base em um cadastro de múltiplas embalagens:

* Embalagem principal: caixa de papelão - acondiciona 2 unidades do produto X;
* Seq.01: pallet - acondiciona 4 caixas de papelão;
* Seq.02: contêiner- acondiciona 5 pallets (seq.01)  
    
  ![image2021-3-3_15-9-5.png](https://tdn.totvs.com/download/attachments/602613977/image2021-3-3_15-9-5.png?version=1&modificationDate=1614800223657&api=v2)

Neste exemplo temos três níveis de embalagens: caixa de papelão para o produto, pallets para as caixas de papelão e contêiner para os pallets.  
Supondo uma venda de 1.000 unidades do produto X teremos:

* quantidade de caixas de papelão = 1.000 (produto X) dividido por 2 (quantidade por caixas de papelão) = 500 unidades;
* quantidade de pallets = 500 (caixas de papelão) dividido por 4 (quantidade por pallet)  = 125 pallets;
* quantidade de contêineres = 125 (pallets) dividido por 5 (quantidade por contêiner)  = 25 contêineres.

Logo o peso bruto será as quantidades de produtos e embalagens vezes os seus respectivos pesos líquidos.

**Embalagens**A seguir serão exibidas as opções disponíveis para a realização do cadastro da embalagem através da rotina EECAT170:

* **Incluir**Possibilita a inclusão de novos cadastros de embalagens que poderão ser associados ao produto pelo cadastro do produto ou diretamente pela manutenção do processo, nas fases de pedido ou embarque de exportação.  
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411446497687/mceclip2.png)  
    
  Além do código e descrição para identificação da embalagem, o peso é fundamental para que se possa obter o peso bruto do item ao qual a embalagem será vinculado.
* ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411441147159/mceclip0.png)
* Nesta tela ainda estarão disponíveis as opções de cadastro da descrição em outros idiomas e a manutenção de múltiplas embalagens, através da opção Outras Ações.  
  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411446241815/mceclip1.png)

* **Alterar**Possibilita a manutenção e atualização das informações dos cadastros existentes, incluindo as opções de descrição em outros idiomas e a manutenção de múltiplas embalagens.

* **Excluir**Possibilita a exclusão dos cadastros de embalagens existentes, uma vez que o cadastro não esteja em uso. Uma vez confirmada a exclusão, o sistema eliminará as descrições desta embalagem em outros idiomas, bem como o vínculo com as demais embalagens em sua hierarquia.

* **Visualizar**Possibilita a visualização do cadastro de embalagem, bem como das descrições em outros idiomas. Acessando a opção de manutenção em Outras Ações será possível visualizar as embalagens desta embalagem, ou seja, o relacionamento de múltiplas embalagens.

**Saiba mais**  
[Embalagens - EECAT170](https://tdn.totvs.com/display/public/PROT/Embalagens+-+EECAT170#Embalagens-EECAT170-eicat170ExemploDeUtilizacao)
