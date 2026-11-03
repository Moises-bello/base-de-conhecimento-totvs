---
article_id: 37153263280279
category: Financeiro - Novo Gestor Financeiro
content_hash: 223047233c17943c41bd144ea2de900b5c529dcc6ef44d0b1179d023dd4c2fdc
fetched_at: '2026-06-28T22:37:41.546588+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Financeiro - FINA710 - Extrato
  API
type: support-article
updated_at: '2025-12-22T11:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37153263280279-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-FINA710-Extrato-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37153232021783) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como realizar a configuração de extrato bancário via API para bancos que ainda não possuem layout configurado no Gestor Financeiro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210

**Solução**

Para configurar a comunicação via API Bancária para a rotina de extrato, a integração utiliza a autenticação mútua de certificados, por isso é necessário que a empresa possua as credenciais de acesso junto à instituição financeira antes de iniciar a configuração no ERP.

Ajustes necessários:

1. Acesse o cadastro de **Parâmetros de Bancos** (FINA130) e identifique o banco disponivel.
2. Configure o campo **Proc. Extrato (EE\_EXTAPI)** com a opção **2 - API Bancaria**;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153263265815)
3. Acesse a rotina **Configuração de Contas** (FINA710);
4. Clique no botão **Novo Layout**;
5. Selecione o banco que deseja cadastrar as credenciais;
6. Na etapa de credenciais, informe o campo **Tipo = Extrato**;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153263266199)
7. Preencha as informações de autenticação fornecidas pelo banco:

   * **Application Key:** Chave de acesso do aplicativo;
   * **Client ID:** Código de identificação do cliente;
   * **Client Secret:** Chave secreta de validação do cliente;
