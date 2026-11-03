---
article_id: 360004194551
category: eSocial - Gerar XML/ Integração Evento
content_hash: 95f2726775b774872999ea84e8b0ae2cd529efa4fb34acc2ad8673b0c89036ec
fetched_at: '2026-06-28T22:47:12.208622+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2299: O campo ''mtvDeslig'' do registro
  ''infoDeslig'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2026-06-26T13:15:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004194551-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2299-O-campo-mtvDeslig-do-registro-infoDeslig-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17460932234775)****Tempo aproximado para leitura: 00:02:30 min**

**Ocorrência**  
Ao gerar o XML do evento S-2299 é retornado o erro **O campo 'mtvDeslig' do registro 'infoDeslig' é obrigatório e não está preenchido**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045012773)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.   
  
**Causa**  
Este problema geralmente acontece por dois motivos: quando realizamos a transferência de um funcionário entre coligadas e o campo **Motivo Saída por Transferência** contido no cadastro de funcionários está em branco; ou quando utilizamos um tipo de desligamento na rescisão para o qual não existe um **De/Para de Desligamento** cadastrado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

* **Funcionário transferido**

1. Acesse o cadastro do funcionário em questão e vá até a aba **Situação**;  
2. Preencha o campo **Motivo Saída por Transferência** com o motivo correto e salve o cadastro;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045013013)

3. Gere novamente o XML do evento **S-2299**. para que o sistema preencha corretamente a *tag* **mtvDeslig**.

* **Funcionário desligado da empresa**

1. Acesse o cadastro da rescisão do funcionário e verifique o **Tipo de Demissão** informado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17457582343319)

2. Alguns tipos de demissão não possuem um de/para interno pelo sistema, sendo necessário então associá-los a um motivo de desligamento do eSocial através do Parametrizador. Sendo assim, acesse o menu **Configurações | Parametrizador | eSocial | De/Para | De/Para de Desligamento**;  
2.1. Faça a inclusão de um novo registro preenchendo o campo **Cód. Tipo Folha de Pagamento** com o tipo de demissão utilizado para rescisão do funcionário e o campo **Cod. Tipo eSocial** com o motivo de desligamento do eSocial, conforme [Tabela 19 do leiaute](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-3-cons-nt-05-2025/tabelas.html#19) e avance para concluir o assistente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17457682866455)

3. Gere novamente o XML do evento **S-2299** para que o sistema preencha a *tag* **mtvDeslig** conforme de/para.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17459145870615)

**Saiba mais**  
Para mais informações acesse:  
      • [Mapeamento evento S-2299](http://tdn.totvs.com/display/LRM/Evento+S-2299)
