---
article_id: 4410156640663
category: eSocial - Tabelas/Não Periódicos
content_hash: 93b4f72fe01772d5f4c906193c525465cc5f51131972fb05e4de317479b52b58
fetched_at: '2026-06-28T22:47:10.344581+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar evento de funcionário: O campo ''tmpParc''
  do registro ''horContratual'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-27T18:24:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410156640663-RH-RM-FOP-eSocial-Erro-ao-gerar-evento-de-funcion%C3%A1rio-O-campo-tmpParc-do-registro-horContratual-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No TOTVS Folha de Pagamento, ao gerar o XML de funcionário (S-2200 e S-2206) ocorre o erro: **O campo 'tmpParc' do registro 'horContratual' é obrigatório e não está preenchido. Erro na validação do campo 'tmpParc': Valores válidos: 0,1,2,3**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre quando o campo **Contrato de trabalho em regime de tempo integral**, presente no cadastro do funcionário, não está preenchido. O campo, conforme leiaute do eSocial, é de preenchimento obrigatório.

![](https://totvssuporte.zendesk.com/attachments/token/lTQK9bNJHBZHBou81bPjRQexx/?name=inline-1270772965.png)

**Solução**Para solucionar o erro, acesse o menu **Administração de Pessoal | Funcionários**, edite o cadastro do funcionário desejado e na aba **Informações Contratuais | Salário/Jornada** preencha o campo **Contrato de trabalho em regime de tempo integral**com a opção que melhor se enquadra a situação do funcionário.

![](https://totvssuporte.zendesk.com/attachments/token/uBJNvif4HP4C5fHq8sLZgRdEO/?name=inline-160267920.png)

**Importante**  
Conforme regra do leiaute, a opção **1 - Limitado a 25 horas semanais** só deve ser utilizada para categoria eSocial igual a **104 - Doméstico**. Já as opções **2 - Limitado a 30 horas semanais** e **3- Limitado a 26 horas semanais** não devem ser utilizadas para a categoria **104**. A categoria pode ser verificada no cadastro do funcionário, aba **Informações Contratuais | Registro**.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Documentação Técnica (Governo)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
