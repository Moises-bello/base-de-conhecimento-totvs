---
article_id: 1500007705742
category: FÉRIAS
content_hash: c624bc9847f3eeb3aa9c7ebcce43739b306d7c2aa648050ecd1513a589ebad88
fetched_at: '2026-06-28T22:44:34.575594+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH -  É possível solicitar férias em data futura
  antes de ter completado o período aquisitivo
type: support-article
updated_at: '2025-12-17T20:20:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007705742-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-solicitar-f%C3%A9rias-em-data-futura-antes-de-ter-completado-o-per%C3%ADodo-aquisitivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28132466820631) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
É possível solicitar férias em data futura antes de ter completado o período aquisitivo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
Por padrão, as férias são solicitadas e calculadas somente após 1 ano completo de Empresa, porém para **o App Meu RH, temos a opção de incluir antes desse período**.  
  
Pensando nessa possibilidade, foi criado o **parâmetro MV\_MRHFERP**, que trará essa possibilidade.  
  
Acesse o módulo **Configurador do Protheus - SIGACFG, em Cadastros > Ambientes > Parâmetros** e o localize  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37100282470679)  
  
No exemplo abaixo, o período aquisitivo é 01/01/2025 até 31/12/2025 e o colaborador possui 27,5 dias de férias proporcionais.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37100282475287)  
  
Caso o parâmetro **MV\_MRHFERP seja igual a .F.**, será possível solicitar férias, desde que a **data de início** **seja após** **31/12/2025**, ou seja de 01/01/2026 em diante (respeitando feriados e DSR).  
  
Caso o funcionário tente solicitar em uma **data anterior a 31/12/2025**, a solicitação não será realizada e a seguinte mensagem será exibida.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37100282477463)  
  
Caso o parâmetro esteja configurado com .T., será possível solicitar normalmente, mesmo antes de 1 ano.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37100323819671)  
  
**Conceito de utilização do parâmetro:**

* Quando definido como **.F.**, o período aquisitivo **em aberto** será exibido apenas para consulta, **não permitindo** a solicitação de férias antes da sua conclusão.
* Quando definido como **.T.**, o período aquisitivo **em aberto** será exibido e **permitirá** que o colaborador realize a solicitação de férias antecipadamente.  
    
  **Saiba Mais**  
  [**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
  [**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
