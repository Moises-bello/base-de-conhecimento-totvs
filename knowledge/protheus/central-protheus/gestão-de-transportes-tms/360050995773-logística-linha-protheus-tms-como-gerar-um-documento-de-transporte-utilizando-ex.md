---
article_id: 360050995773
category: Gestão de Transportes (TMS)
content_hash: 99037fd090a9b062cf9a934c76803a18f73d2c5cb09b626d7c1d00a50fa2e0c1
fetched_at: '2026-06-28T22:45:27.468894+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como gerar um documento de transporte utilizando
  Exceções Fiscais
type: support-article
updated_at: '2021-07-19T12:57:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050995773-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-um-documento-de-transporte-utilizando-Exce%C3%A7%C3%B5es-Fiscais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:10 min  
  
Dúvida**Qual a parametrização necessária para que o cálculo de frete utilize as exceções Fiscais?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O cálculo de documento com Exceção Fiscal pode ser utilizado em situações onde a regra de tributação ou as configurações padrão do Protheus não atendam alguma particularidade.

1. **Cliente.**Acessar o menu **Atualizações/Cadastros/Clientes - MATA030.**O Cliente devedor do frete deve ter estes campos definidos:  
   **Aba Fiscais:  
   A1\_GRPTRIB - Grp.Clientes** = Grupo de tributação
2. **Produto de Cálculo**. Acessar o menu **Atualizações/Cadastros/Produtos - MATA010.** Este produto é utilizado para a escrituração do documento que será emitido no **TMS - Transportation Management System** e é vinculado ao cadastro de Configuração documento localizado no menu **Atualizações/Documentos e Regras/Config. Documentos - TMSA150**.

   Neste cadastro devem ser considerados os campos:  
   **Aba Impostos:  
   B1\_GRTRIB - Grupo Trib.** = Código do Grupo de Tributação.
3. **Exceções Fiscais**. Acessar o menu **Atualizações/Documentos e Regras/Exceções Fiscais -****MATA540.**Neste cadastro devem ser considerados os campos:  
   **F7\_GRTRIB - Grupo Trib.** = Informar o mesmo código do campo **Grupo Trib.** do cadastro de **Produtos - MATA010**.  
   **F7\_EST - Estado** = Informar o estado de destino para o qual o produto está sendo enviado.  
   **F7\_ALIQINT - Aliq.Interna** ou **F7\_ALIQEXT - Aliq.Externa. =** Informar a alíquota interna e externa conforme exceção fiscal.  
   **F7\_GRPCLI - Grp.Cli/For** = Informar o mesmo código do campo **A1\_GRPTRIB -****Grp.Clientes** do cadastro de **Clientes - MATA030**.  
     
   Quando efetuar o cálculo de frete para um cliente devedor que esteja relacionado a um **A1\_GRPTRIB - Grp.Clientes**da **Exceção Fiscal**,o Sistema deverá respeitar as regras definidas no cadastro.
