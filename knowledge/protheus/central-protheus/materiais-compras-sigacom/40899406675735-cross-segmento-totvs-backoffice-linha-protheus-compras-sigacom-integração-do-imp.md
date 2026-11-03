---
article_id: 40899406675735
category: Materiais - Compras (SIGACOM)
content_hash: 4302ead0235382a7453a8f2ee7450e149c2d07eb1ebfbc3749da087d278f2c2f
fetched_at: '2026-06-28T22:41:07.312580+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras (SIGACOM) - Integração
  do Importador XML com o Configurador de Tributos (FISA170)
type: support-article
updated_at: '2026-06-02T12:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40899406675735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Compras-SIGACOM-Integra%C3%A7%C3%A3o-do-Importador-XML-com-o-Configurador-de-Tributos-FISA170
---

### **Dúvida**

Como realizar o cálculo automático de impostos por meio das regras do Configurador de Tributos (FISA170) durante o processo de recebimento de notas fiscais eletrônicas utilizando a rotina do Importador XML?

### **Ambiente**

Cross Segmento – TOTVS Backoffice (Linha Protheus) – Compras (SIGACOM) – Importador XML – A partir da Versão 12.

### **Solução**

Foi implementada uma alteração estrutural na rotina do Importador XML para integrar o cálculo de impostos nativo ao **Configurador de Tributos (FISA170)**. A partir desta atualização, ao manipular os dados no monitor de recebimento, o sistema valida dinamicamente se o fornecedor, o produto e o código de operação atendem aos critérios tributários predefinidos, carregando os valores dos impostos automaticamente de forma transparente.

1. ### Carregando impostos no monitor

Após concluir a configuração dos tributos ([FISA170](https://tdn.totvs.com/x/5SApK)), acesse o monitor (COMXCOL) através do menu: **Miscelânea/Importador de XML/monito**r.

Ao entrar no monitor e adicionar/modificar o CFOP de entrada (**DT\_CODCFEN**) de um registro, se o **fornecedor**e **produto**estiverem em conformidade com as regras cadastradas no configurador de tributos, os valores dos impostos serão automaticamente carregados.

No exemplo abaixo, foi previamente configurada uma regra no configurador de tributos ([FISA170](https://tdn.totvs.com/x/5SApK)) para o valor do ICMS, com uma alíquota de 50%, aplicável aos CFOPs: **1111**e **2111**:

Ao inserir o **CFOP**, caso o **fornecedor**e **produto**atendam às regras cadastradas no configurador, o sistema carregará automaticamente o valor do ICMS conforme a regra estabelecida:

![cfop de entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/40899399520023)

2. ### Geração do documento classificado

Ao gerar o documento **classificado**, a nota já incluirá automaticamente os impostos do configurador de tributos.

![trib classificado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/40899399520791)

3. ### Geração da Pré-Nota

Ao gerar o documento como pré-nota, a mesma já incluirá automaticamente os impostos do configurador de tributos, sendo assim, ao classificar o documento,  os impostos poderão ser mantidos caso não seja alterado o D1\_CF.

![trib pre nota.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/40899425753879)

### Observações

Ao inserir ou modificar uma TES (**DT\_TES**) que contenha o campo (**F4\_CF**) preenchido em seu cadastro, se o CFOP (**F4\_CF**), **fornecedor**e **produto**estiverem em conformidade com as regras cadastradas no configurador, os valores dos impostos serão automaticamente carregados. Neste cenário, ao digitar o CFOP (**DT\_CODCFEN**), os valores serão novamente carregados, uma vez que a regra do configurador é específica para o CFOP.

### **Saiba Mais**

* [IX14 - Importador XML x Configurador de Tributos - Documentação de Referência](https://www.google.com/search?q=https://tdn.totvs.com/display/public/PROT/IX14%2B-%2BImportador%2BXML%2Bx%2BConfigurador%2Bde%2BTributos)
* [CFGTRIB - Operandos de Integração](https://tdn.totvs.com/pages/releaseview.action?pageId=932351237)
