---
article_id: 360004475572
category: Administração de Pessoal
content_hash: d6785991464bc850dcf3d0814b91717785cb7ceaba764f1b34a3001e21cbdfe3
fetched_at: '2026-06-28T22:47:02.399114+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Licença Maternidade por Adoção
type: support-article
updated_at: '2026-05-27T17:27:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004475572-RH-RM-FOP-Licen%C3%A7a-Maternidade-por-Ado%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15668936651543) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como efetuar o lançamento de Licença Maternidade por Adoção?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para efetuar o lançamento da Licença Maternidade por Adoção deverá seguir os seguintes passos:  
  
1. No módulo Folha de Pagamento acesse o menu **Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas,** e na tabela dinâmica **INT28 - Motivo de Mudança de Situação** crie um motivo exclusivo para Licença Maternidade por adoção. Exemplo: **13 - Licença Maternidade por Adoção.**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016817871)  
  
2. Acesse o menu **Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Salário Maternidade 2/2** e preencha o campo **Motivo de afastamento ref . a licença maternidade por adoção** com o motivo especifico criado na tabela dinâmica **INT28 - Motivo de Mudança de Situação**:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011478482)**3. Para considerar o afastamento Licença Maternidade pago pela Previdência deverá alterar a situação da funcionário para **E - Licença Mater.** e o motivo **13 - Licença Maternidade por Adoção**:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360005700411)  
  
4. Para o pagamento é necessário que, acesse o menu **Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Salário Maternidade 1/2** e habilite a flag **Salário Maternidade pago pela Previdência,** e informe os eventos nos campos **Eventos salário maternidade pago pela previdência** e **Evento de média salário maternidade pago pela previdência**:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011746721)  
 **Importante**Os eventos devem ser do tipo base de cálculo e sem código de cálculo. A incidência deverá ser **apenas** em FGTS. Caso não possua os eventos, deverão ser criados através do menu **Administração de Pessoal | Eventos | Eventos**.  
  
**Saiba mais**[Salário Maternidade 1/2](https://tdn.totvs.com/pages/releaseview.action?pageId=452719554)[Salário Maternidade 2/2](https://tdn.totvs.com/pages/releaseview.action?pageId=452719874)  
Para mais informações sobre a legislação vigente sobre o tema, [CLIQUE AQUI](https://www.empresario.com.br/legislacao/edicoes/2011/licenca_maternidade_adocao.html).
