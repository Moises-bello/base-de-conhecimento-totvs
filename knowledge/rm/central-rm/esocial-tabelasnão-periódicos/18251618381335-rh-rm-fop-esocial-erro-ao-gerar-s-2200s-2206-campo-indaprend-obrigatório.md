---
article_id: 18251618381335
category: eSocial - Tabelas/Não Periódicos
content_hash: 5eb08b09cc5f7550ae19b3c11205c319f73cb4959b9101338bbe7a6df7d55693
fetched_at: '2026-06-28T22:47:10.358084+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2200/S-2206: campo ''indAprend''
  obrigatório'
type: support-article
updated_at: '2024-12-30T13:55:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18251618381335-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2200-S-2206-campo-indAprend-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18251588147991)  Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar XML do evento S-2200 ou S-2206 são apresentadas as mensagens **O campo 'indAprend' do registro 'aprend' é obrigatório e não está preenchido.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251207774487)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos Patches 12.1.2302.235, 12.1.2306.182 e 12.1.2310.116  
  
**Causa**Esse incidente ocorre quando no cadastro do funcionário **aprendiz** (categoria eSocial 103), menu **Registro**, aba **Dados do Aprendiz**, foi informada modalidade de contratação **Indireta**, mas não foi informado o **CNPJ/CPF do empregador cotista**.

                                                 

**Solução**Conforme leiaute do eSocial, o grupo **aprend** é obrigatório quando a categoria do eSocial for **103** (Empregador - Aprendiz) e data de admissão ou alteração for maior ou igual a 22/01/2024. Dentro do grupo **aprend**, o campo **indAprend** é obrigatório, sendo assim, é necessário preencher o campo para correta geração do grupo.

*Leiaute S-1.2 - S-2200*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251277846935)

*Leiaute S-1.2 - S-2206*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251263106583)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251603426455)

Para correção, no cadastro do funcionário, menu **Registro**, aba **Dados do Aprendiz**, informe a modalidade de contratação (direta ou indireta) e preencha o campo CNPJ Entidade Qualificadora/Empregador Cotista:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18251431441559)

**Saiba mais**  
Para mais informações sobre a contratação de aprendiz, acesse:

* [Contratação de Aprendiz - Leiaute S-1.2](https://tdn.totvs.com/pages/viewpage.action?pageId=795092070)
