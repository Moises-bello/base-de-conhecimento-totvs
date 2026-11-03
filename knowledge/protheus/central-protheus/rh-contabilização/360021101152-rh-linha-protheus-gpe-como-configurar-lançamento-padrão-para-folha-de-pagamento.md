---
article_id: 360021101152
category: RH - Contabilização
content_hash: 23f7e583fdbf4f7ab691d6f86e1f2ae853832119263e137b7d24ff9eea420e2e
fetched_at: '2026-06-28T22:43:45.795425+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de
  Pagamento ou Provisão no Protheus
type: support-article
updated_at: '2025-11-03T21:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-ou-Provis%C3%A3o-no-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17205352829719)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como configurar um lançamento padrão para contabilizar as verbas de Folha de Pagamento ou provisão no Protheus?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Esse cadastro é o elo entre o modulo GPE e o módulo Contabilidade Gerencial. Toda a integração contábil é feita a partir dos dados e regras cadastradas.   
  
Atenção:   
O passo a passo abaixo é apenas uma demonstração de como as informações em cada campo serão tratadas no funcionamento da rotina. 

No menu do SIGAGPE, acesse: **Atualizações -> Cadastros -> Lançamentos Padrões -> Incluir/Alterar**Os lançamentos do módulo Gestão de Pessoal devem ter códigos entre **A01 e Z99. Não há Lançamentos padrões específicos para verbas da folha ou para verbas da provisão.**

A tela de inclusão é apresentada, dividida em pastas:

**Cadastro****![kcscontabil01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017913531)**

**Entidades**Cada campo tem uma consulta associada, na qual é possível selecionar o tipo de dado que será afetado. É possível eleger entre o classificador contábil (conta, item contábil, centro de custo ou classe de valor):

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018031552)**

**Obs.:** Insira uma conta débito e conta crédito válida. ou uma fórmula para busca das contas.   
  
**Valores**Nesta pasta é registrado o valor que terá o lançamento contábil configurado. Os campos disponíveis permitem salvar o valor do lançamento contábil em cada moeda; dessa maneira, os campos podem aceitar as fórmulas que retornem valores numéricos. Para contabilizar valores do SIGAGPE, os dados devem ser buscados da tabela SRZ (Temporária no momento da contabilização, que pode conter dados da folha e/ou provisão - tanto aberta quanto fechada):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018031632)

**Histórico**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074588094)  
 **Histórico:** SRZ->RZ\_PD+" "+POSICIONE("SRV",1,XFILIAL("SRV")+SRZ->RZ\_PD,"SRV->RV\_DESC")  
 **OBS.:** Lembrando que deve-se ter cuidado nas fórmulas utilizadas devido a questão de performance (demora na geração da contabilização).  
  
**Dica:** Caso tenha dúvidas na sua configuração, teste utilizando um campo fixo no LP que apresenta o erro, retirando as customizações ou sintaxes ADVPL.  
  
Necessitando de apoio na configuração/validação do lançamento padrão, entre em contato com seu gerente de contas TOTVS, e solicite o agendamento de um analista in loco , uma vez que este atendimento é realizado somente através de consultoria. 

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
