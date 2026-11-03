---
article_id: 360036252253
category: Portal de Gestão de Capital Humano
content_hash: d21317fc0e51cf72daa3c22cc4189070093e21e8fca3f43fc145452adc13f5da
fetched_at: '2026-06-28T22:42:59.126481+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Atualize o fonte CRIAOBJ.JS através do Wizard
type: support-article
updated_at: '2021-09-29T13:13:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036252253-RH-Linha-Protheus-PORTAL-GCH-Atualize-o-fonte-CRIAOBJ-JS-atrav%C3%A9s-do-Wizard
---

**Dúvida**Como resolver a mensagem - Atualize o fonte CRIAOBJ.JS através do Wizard?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano - Todas as versões  
  
**Solução**Para solucionar essa mensagem, realize os seguintes passos:

1. Baixe a atualize o ambiente com o último Binário e Pacote Acumulado de RH do Portal:  
[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848-MP-GPE-Pacote-de-acumulado-do-RH-no-Portal-de-Cliente)  
  
2. Baixe os arquivos do Portal - *web-files,*disponível no Portal do Cliente:  
[MP - PORTAL GCH - Como Atualizar os arquivos do Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613-MP-PORTAL-GCH-Como-Atualizar-os-arquivos-do-Portal)  
  
3. Descompacte o arquivo baixado no item 2 no diretório *systemload* do protheus. Para atualizar deve acessar o Totvs *Wizard,* alterar a configuração do *Web Service (ws)* e ir diretamente no Avançar, então o sistema apresentará uma mensagem se deseja descompactar o pacote, informe sim e clique em avançar. Depois, deverá fazer o mesmo processo porém na configuração do PP (Portal RH).  
**Obs**.: Esta orientação também consta no link do item 2.  
  
4. A mensagem também pode ser apresentada porque não há nenhum usuário de portal associado a este Participante. Assim, acesse o módulo 53 (Avaliação e Pesquisa de Desempenho), vá no cadastro do participante (alterar) e amarre um usuário de portal no campo **Usuário Portal**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098634734/mceclip0.png)  
  
Com esses 4 procedimentos, vai funcionar corretamente.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo: [CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
