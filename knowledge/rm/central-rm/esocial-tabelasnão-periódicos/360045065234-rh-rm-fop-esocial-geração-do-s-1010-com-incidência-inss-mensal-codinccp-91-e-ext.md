---
article_id: 360045065234
category: eSocial - Tabelas/Não Periódicos
content_hash: 0f1eba2baab1ce9a59722e0069bde4ee7703de8a88e242dcad8f44da4aadad43
fetched_at: '2026-06-28T22:47:10.478912+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Geração do S-1010 com Incidência INSS Mensal (codIncCP
  = 91) e extensão da decisão judicial somente da contribuição previdenciária patronal
  (extDecisao = 1)
type: support-article
updated_at: '2025-07-02T17:36:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045065234-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-S-1010-com-Incid%C3%AAncia-INSS-Mensal-codIncCP-91-e-extens%C3%A3o-da-decis%C3%A3o-judicial-somente-da-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-patronal-extDecisao-1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24447598510615)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar S-1010 com Incidência INSS Mensal (codIncCP = 91) e extensão da decisão judicial somente da contribuição previdenciária patronal (extDecisao = 1).  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Conforme Manual de Orientações do eSocial, quando houver decisão judicial somente à alíquota Patronal, RAT e contribuição destinada a outras entidades, esta informação deve ser refletida no campo {extDecisão} com o código [1] – “Contribuição Previdenciária Patronal”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24448557274135)

• Configuração do **código de incidência**  
Para informar a *tag***codIncCP = 91-Mensal**, siga os passos abaixo:

1. Acesse **Administração de Pessoal | Eventos;**2. Selecione o evento e clique em **Editar**;  
3. Acesse a aba **Inc. Proventos**, e marque as incidência Folha em **INSS;**  
4. Informe no campo **Exclusiva do e Empregador** o valor **91 - Mensal**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24448535758615)

• Configuração para informar a **Extensão da Decisão/Sentença** no cadastro do Evento - *tag***extDecisao =1 - Contribuição Previdenciária Patronal**

1. Acesse**Anexos | Processo de Suspensão de Incidência** e inclua um novo registro;  
2. Selecione a opção **Contrib.Patronais** do campo **Extensão da Decisão/Sentença**.

Abaixo um exemplo da parametrização:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063342933)

3. Gere o XML do evento S-1010 com a competência desejada e integre com o governo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24448535765911)

**Saiba mais**  
Para mais informações sobre geração do XML acesse:  
      • [Como gerar a tag codIncCP com a incidência 91 e extensão da decisão/sentença(Contrib Patronais=1)](https://tdn.totvs.com/pages/releaseview.action?pageId=520667406)   
      • [Cadastro do evento S-1070 Tabela de Processos Administrativos/Judiciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008847432-RM-eSocial-Cadastro-do-evento-S-1070-Tabela-de-Processos-Administrativos-Judiciais)  
     • [Mapeamento Evento S-1010](https://tdn.totvs.com/display/public/LRM/Evento+S-1010)
