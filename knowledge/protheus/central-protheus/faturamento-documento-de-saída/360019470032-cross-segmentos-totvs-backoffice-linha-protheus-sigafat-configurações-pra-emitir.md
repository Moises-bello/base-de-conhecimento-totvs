---
article_id: 360019470032
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c884a76b816c7a17d7cb37053bcdc86acc56462dba1fac4c0d9b6b75979235f8
fetched_at: '2026-06-28T22:38:45.061704+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configurações
  pra emitir e impedir a geração de uma Nota Fiscal Retroativa
type: support-article
updated_at: '2022-03-02T20:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019470032-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%B5es-pra-emitir-e-impedir-a-gera%C3%A7%C3%A3o-de-uma-Nota-Fiscal-Retroativa
---

**Dúvida**

 Configurações pra emitir e impedir a geração de uma Nota Fiscal Retroativa.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT– A partir da release 11.80.  
  
**Solução**

Para realizar a emissão de uma nota com data retroativa, deve-se respeitar os seguintes parâmetros:

 

* A nota não pode ser maior a 60 dias retroativos;
* O parâmetro MV\_AUTOEMI deve estar configurado com a quantidade de dias necessários para a emissão da nota;
* O cadastro de usuários deve ter permissão para realizar emissões com datas retroativas;

+ SIGACFG pergunta 51.

 

**1- Emissão do documento de saída:**

 

* Voltar a data base do sistema para a data desejada;
* Incluir um pedido de venda MATA410;
* Preparar documento de Saída MATA460A;
* Verificar se os campos F2\_EMISSAO, FT\_EMISSÃO, F3\_EMISSÃO e D2\_EMISSÃO estão com a data retroativa:

 ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046901333/mceclip0.png)

Se tudo estiver correto, basta transmitir a nota.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**2 - Impedir a emissão da nota retroativa:**

Para impedir apenas a Emissão de Nota, há a restrição de acesso por usuário N. 51 para a rotina **MATA460A** que deve ser desmarcada.

Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse o **Configurador SIGACFG**;  
2. Acesse **Usuário**;  
3. Acesse **Senhas**;  
4. Acesse **Usuário**;  
5. Selecione o **Usuário** e clique em **Alterar**;  
6. Acesse a aba **Restrições de acesso**;  
7. Acesse a aba **Acessos**;  
8. Procure a opção **51 Emitir NF Retroativa**;  
9. Nessa opção você ira marcar para emitir, e desmarcar para não emitir.

Obs..Em caso de vendas retroativas por PDV ou Venda assistida, contate a equipe de Automação comercial para validar o processo a ser efetuado.

**Saiba Mais:  
[Impedir emissão de Nota de Saída com Data Retroativa](http://tdn.totvs.com/pages/releaseview.action?pageId=272705839)**
