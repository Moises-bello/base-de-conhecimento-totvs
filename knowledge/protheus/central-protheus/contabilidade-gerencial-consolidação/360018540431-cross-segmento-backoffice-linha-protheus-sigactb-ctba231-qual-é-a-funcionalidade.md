---
article_id: 360018540431
category: Contabilidade Gerencial - Consolidação
content_hash: c98f8f5ba9713f9d6d6de8aa1b256bb40e66bc5328c1bbde7553374bcbbad9e5
fetched_at: '2026-06-28T22:40:56.802134+00:00'
product: protheus
section_id: 1500001548562
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA231 Qual é a funcionalidade
  da rotina Consolidação Configurada 2 ?
type: support-article
updated_at: '2023-11-14T19:12:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018540431-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA231-Qual-%C3%A9-a-funcionalidade-da-rotina-Consolida%C3%A7%C3%A3o-Configurada-2
---

**Dúvida**Qual é a funcionalidade da rotina Consolidação Configurada 2 (CTBA231)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Contabilidade Gerencial – Todas as versões  
  
  
**Solução**

Esta rotina realiza a consolidação dos lançamentos contábeis, diferentemente da Consolidação Configurada (CTBA230) que realiza a consolidação dos lançamentos contábeis pelo saldo.

Para a CTBA231 é necessário configurar o parâmetro **MV\_CONSOLD** com o código e a filial da empresa consolidadora.

**Procedimentos**

**Importante!**

Ao acessar o Sistema, pelo Protheus Remote, informe a senha de acesso e selecione a empresa consolidadora.

1. Acesse o módulo **Contabilidade Gerencial** na opção **Atualizações/Cadastros/Roteiro Consolidação (CTBA240)** e para cadastrar um roteiro de consolidação, clique em **Incluir**.  
2. Utilize lançamentos diversos ou lançamentos já existentes em duas ou mais empresas/filiais diferentes.  
3. Na tela de cadastro do roteiro, observe o campo **Hist. Aglutinador** e informe se desejar um histórico específico.  
4. Cada roteiro pode utilizar mais de uma linha.

**Importante!**

O campo **Fórmula** quando preenchido, terá esse conteúdo utilizado no preenchimento do histórico do lançamento contábil, gerado na empresa consolidadora. Se o campo **Fórmula** não for preenchido, o histórico utilizado será o conteúdo do campo **Hist. Aglutinador**, que está no cabeçalho do cadastro de roteiro de consolidação. Confirme a execução conforme a configuração definida.

5. O Sistema exibe uma mensagem de advertência para a necessidade de uso exclusivo. Verifique e confirme.  
6. Visualize a tela explicativa da Consolidação de Empresas/Filiais.  
7. Clique no botão **Parâmetros** e configure-os com a ajuda do help de campo.  
8. Ao final o Sistema exibe a tela para confirmação dos dados incluídos
