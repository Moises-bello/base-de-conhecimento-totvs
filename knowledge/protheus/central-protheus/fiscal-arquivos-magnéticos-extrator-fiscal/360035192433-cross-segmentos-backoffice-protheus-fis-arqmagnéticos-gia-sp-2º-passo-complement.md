---
article_id: 360035192433
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: a00f68c9dc3914fac100c93ba4673ba96d9041c6fa9671aa063a3d21335fba30
fetched_at: '2026-06-28T22:42:07.795574+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 2º
  Passo - Complemento Cadastral
type: support-article
updated_at: '2024-06-04T19:01:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035192433-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-SP-2%C2%BA-Passo-Complemento-Cadastral
---

**Ocorrência**Necessário atualizar o ambiente TAF para utilização da GIA-SP.  
  
**Ambiente**Protheus - Livros Fiscais – A partir da versão 12.1.17.  
 **Causa**Necessidade das configurações para a geração do arquivo da **Nova GIA**através do **TAF**.  
 **Solução**

Agora que o ambiente está atualizado com as últimos pacotes disponíveis, iniciaremos a configuração dos parâmetros essenciais para correto funcionamento do processo.   
  
O Complemento de Empresa é o cadastro responsável por contemplar diversas informações da empresa/estabelecimento, além da configuração de filiais de destino das integrações destinadas a base de dados do TAF e das obrigações fiscais geradas pelo estabelecimento.  
  
Obs.: O procedimento que demonstraremos a seguir é valido para gerar o arquivo da GIA. Caso tenha dúvidas com relação à configuração para demais obrigações, consulte o TDN e/ou a equipe de suporte responsável pela Obrigação Fiscal a ser entregue.   
  
Para configuração do complemento cadastral para gerar a GIA acesse: **84-TOTVS Automação Fiscal -> Atualizações -> Configs. Taf. -> Complemento Cadastral** e acione a opção Incluir.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058176894)  
  
Pasta: **Complemento do Estabelecimento/Informações do Estabelecimento**  
  
**Filial TAF**= Informe o Código da Filial a ser utilizada pelo TAF.  
**Cód. Filial** = Informe o Código da Empresa+Código da Filial.

![](https://tdn.totvs.com/download/attachments/379308197/image2018-7-4_13-12-12.png?version=1&modificationDate=1530720733000&api=v2)

Pasta: **Complemento do Estabelecimento/Obrigações Fiscais**  
  
**Código Obrig.** = Informe o código da Obrigação Fiscal. 

![](https://tdn.totvs.com/download/attachments/379308197/image2018-7-4_13-12-28.png?version=1&modificationDate=1530720749000&api=v2)

Após concluir as configurações acione a opção **Confirmar**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045901753)

![](https://tdn.totvs.com/download/attachments/379308197/image2019-8-21_11-56-42.png?version=1&modificationDate=1566399402957&api=v2)
