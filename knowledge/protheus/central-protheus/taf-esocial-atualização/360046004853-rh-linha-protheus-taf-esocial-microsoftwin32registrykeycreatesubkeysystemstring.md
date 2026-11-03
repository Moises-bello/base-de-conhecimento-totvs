---
article_id: 360046004853
category: TAF - eSocial - Atualização
content_hash: 5b49f87239fb2a6bbbe14542371b2f9456136cb68ea5eea540b87dce10655a56
fetched_at: '2026-06-28T22:45:13.408753+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Microsoft.Win32.RegistryKey.CreateSubKey(System.String,
  Boolean)
type: support-article
updated_at: '2024-05-29T17:23:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046004853-RH-Linha-Protheus-TAF-eSocial-Microsoft-Win32-RegistryKey-CreateSubKey-System-String-Boolean
---

**Dúvida**

Durante o processo de instalação ou atualização do TAF, através do atualizador, você pode encontrar o seguinte erro no log:

*"OCORREU UM ERRO NÃO TRATADO! Método não encontrado: 'Microsoft.Win32.RegistryKey Microsoft.Win32.RegistryKey.CreateSubKey(System.String, Boolean)'"*

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Solução**

**Importante:** Esta solução deve ser executada pela equipe de infraestrutura da sua empresa.

**Observação:**

Certifique-se de que o sistema operacional esteja em conformidade com os requisitos mencionados no seguinte link no TDN:

<https://tdn.totvs.com/pages/viewpage.action?pageId=452690307>

1. Verifique a Versão do .NET Framework: É possível que o problema esteja relacionado à versão do .NET Framework instalado no seu sistema operacional Windows. Verifique se a versão é igual ou superior a 4.6.1.
2. Baixe a Versão Atualizada do .NET Framework: Acesse o site da Microsoft e faça o download da versão do .NET Framework igual ou superior a 4.6.1. Isso garantirá a compatibilidade adequada para o funcionamento do TAF.
3. Identificando sua Versão Atual do .NET Framework: Para verificar a versão atual do .NET Framework, siga os passos abaixo:

   * Acesse o Painel de Controle do Windows.
   * Clique em "Programas".
   * Selecione "Ativar ou desativar recursos do Windows".
   * Nesta tela, você poderá identificar as versões do .NET Framework instaladas.  
     ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063489414)
4. Configurando a Nova Versão do .NET Framework: Após baixar e instalar a versão adequada do .NET Framework, retorne ao processo de instalação ou atualização do TAF e TSS.
