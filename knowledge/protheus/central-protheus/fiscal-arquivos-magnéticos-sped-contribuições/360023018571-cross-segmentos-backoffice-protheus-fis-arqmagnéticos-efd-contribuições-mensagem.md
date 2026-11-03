---
article_id: 360023018571
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 6238fb799b8158c3b78bead06b2725f0c046242d4745400678c52090b7bd6956
fetched_at: '2026-06-28T22:42:05.221082+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Mensagem de erro de compartilhamento de tabelas
type: support-article
updated_at: '2023-01-04T17:25:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023018571-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Mensagem-de-erro-de-compartilhamento-de-tabelas
---

**Ocorrência**  
Após processar a apuração do **EFD Contribuições** ocorre a seguinte mensagem "Atenção, o compartilhamento das tabelas abaixo não condizem com o modo de apuração selecionado **CCY, CCW, SFV, SFW, CF5, CF4, CF3**"

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Esse incidente ocorre, devido a opção de gravação utilizada na pergunta da *Wizard* e o compartilhamento das tabelas estarem divergentes.  
   
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Para gerar a apuração da Matriz e Filial separadas, escolha a opçãode gravação **Individualiza** da *Wizard* e depois clique o botão **Agrupar Filial -> Matriz** para a geração do arquivo.  
  
 2. Para gerar a apuração da Matriz e da filial de forma agrupada, escolha a opção de gravação **Agrupada** da *Wizard*.  
  
 3. Apurações distintas por filial: Há duas formas de realizar apuração, a primeira é de forma já agrupada, onde todas as informações e valores serão agrupadas na matriz (empresa logada), gerando assim somente uma apuração contendo todos os valores de todas as filiais.   
Para isto a pergunta Opção Gravação deverá estar com opção **“Agrupada”**. Desta maneira as tabelas **CCY,CCW,CF4,CF3,SFV e SFW**  devem estar como "Compartilhadas".  
  
4. A segunda forma é processar as apurações por filial, onde cada filial terá a sua apuração, e quando todos os valores estiverem validados, posteriormente as informações deverão ser consolidadas. Para isto, a pergunta Opção Gravação deverá estar com opção “**Individualizada**”, para que as apurações sejam geradas individualmente. Após a conferência das informações pelo usuário, clique na opção **Agrupar Filial->Matriz e** informe em qual empresa as apurações deverão ser consolidadas, em seguida preencha qual período das apurações deverá ser considerado para agrupar e selecionar quais filiais deverão ter as apurações consolidadas.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020376251/Capturar.PNG)

![Capturar3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360020493732/Capturar3.PNG)
