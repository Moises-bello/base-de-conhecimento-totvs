---
article_id: 360056309114
category: eSocial - Parametrizador
content_hash: 1d0113b8c64267a76f7785a1f52653f07129fe7ce957b0b10197ba808647add8
fetched_at: '2026-06-28T22:47:06.330701+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - De/Para de afastamento eSocial
type: support-article
updated_at: '2025-11-05T19:02:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056309114-RH-RM-FOP-eSocial-De-Para-de-afastamento-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23005106192151)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como realizar De/Para de afastamento para envio ao eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as versões  
  
**Solução**Através deste processo o usuário poderá relacionar o código de afastamento da folha de pagamento com alguns códigos de afastamento relacionados conforme a **Tabela 18** do eSocial. Abaixo o passo a passo.

**1.** No Módulo **Folha de Pagamento** acesse **Configurações | Parametrizador | eSocial | De/Para de afastamento** e inclua o **Código Tipo Labore** vinculado ao **Código Motivo eSocial**. 

![NOVO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097881153)

**• Cód. Tipo Labore**  
Poderá selecionar os tipos U(Outros), C(Contrato de Trabalho Suspenso) e Y(Licença Paternidade). Esses tipos de afastamento não possuem relacionamento específico na Tabela 18 do eSocial.

**• Cód. Motivo Labore**Poderá selecionar qualquer motivo de afastamento. Esse motivo é parametrizável por tabelas dinâmicas no TOTVS Folha de Pagamento.

**• Cód. Motivo eSocial**Poderá selecionar o motivo de afastamento conforme a **Tabela 18** do eSocial que desejar.  
  
**2.** Em seguida, no cadastro do funcionário acesse o anexo **Históricos |** **Histórico de Afastamento,** inclua um novo afastamento e preencha com os dados informados no parâmetro do eSocial.

![FSA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097875453)

3. Na geração do XML do evento **S-2230- Afastamento Temporário**, será considerado o **Cód. Motivo eSocial 16** conforme parametrizado.

![xml.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097876753)

**Importante**  
Os valores parametrizados no **De/Para de Afastamento**s terão prioridade sobre qualquer de/para que é feito internamente pelo sistema.  
  
**Saiba mais**  
Para mais informações acesse:  
      • [S-2230 - Afastamento Temporário](https://tdn.totvs.com/pages/releaseview.action?pageId=364908488)
