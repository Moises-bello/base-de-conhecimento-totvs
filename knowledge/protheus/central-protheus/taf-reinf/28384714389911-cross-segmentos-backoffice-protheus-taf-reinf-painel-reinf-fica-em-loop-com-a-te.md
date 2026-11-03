---
article_id: 28384714389911
category: TAF - REINF
content_hash: 4c44ac10197f93ac18c6bfee808c8b6640d497c7a103d82208dc438858799923
fetched_at: '2026-06-28T22:41:34.741804+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Painel REINF fica em
  loop com a tela em Branco.
type: support-article
updated_at: '2026-06-09T18:09:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28384714389911-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Painel-REINF-fica-em-loop-com-a-tela-em-Branco
---

**Ocorrência**  Ao acessar a rotina ***TAFA552B***-Painel REINF a rotina é aberta e fica em loop constante com a tela em branco não habilitando as opções da rotina.

![tela em branco painel.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28384795005463)

**Ambiente**A partir de 12.1.2210  
  
**Causa** O incidente pode ocorrer devido há uma serie de fatores estruturais, configuração da rotina, atualização do ambiente, uso do sistema operacional não homologado, abaixo recomendações de analise.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Exclua sua pasta app-root dentro da estrutura do seu ambiente para ser recriada.

2.  Verifique se o seu ambiente está configurado com a porta multi protocolo e os parâmetros MV\_BACKEND e MV\_GCTPURL estão em branco, conforme o KCS abaixo.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Configuração Painel Reinf utilizando MPP - Porta Multiprotocolo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415235211799-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-utilizando-MPP-Porta-Multiprotocolo)

3. O ambiente deve está com a release homologado do sistema e com ultimo acumulado do TAF disponível do portal aplicado.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Atualização Completa Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-Reinf)

4.  Para manter o ambiente com Binário e LIB atualizado e ter o correto comportamento da rotina é necessário que o servidor instalado o seu ambiente esteja com sistema operacional homologado.

Segue lista dos Sistemas Operacionais homologados para uso do AppServer e DBAccess <https://tdn.totvs.com/display/tec/Application+Server+19.3.0.x+e+superiores+-+Sistemas+operacionais>

Lista dos homologados para uso do SmartClient <https://tdn.totvs.com/display/tec/SmartClient>  
 

5. Atualize o seu APPSERVER e SMARTCLIENT com o ultimo disponível no portal.

Portal Smartclient: <https://suporte.totvs.com/portal/p/10098/download?e=1050526#000006/368/TFSC/>

Portal Appserver: <https://suporte.totvs.com/portal/p/10098/download?e=1050526#000006/368/TFAPP/>

**IMPORTANTE: Duvida relacionadas sobre este comportamento( passo 4 e 5), deverá ser avaliada em um chamado com time de suporte framework.**

5. Reinicie os serviços abaixo.

-> Servidor de licenças  
-> Dbaccess  
-> Appserver  
-> Demais serviços
