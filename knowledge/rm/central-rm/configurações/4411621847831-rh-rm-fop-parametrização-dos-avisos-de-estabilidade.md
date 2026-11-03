---
article_id: 4411621847831
category: Configurações
content_hash: 147dc78d95345b312c54eb71fb88c8186de0956d4a505e7a0b32bb85544d675e
fetched_at: '2026-06-28T22:46:49.571568+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Parametrização dos Avisos de Estabilidade
type: support-article
updated_at: '2024-10-18T15:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411621847831-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-dos-Avisos-de-Estabilidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27165807370263) Tempo aproximado para leitura: **00:0****2:40 min****Dúvida**Como parametrizar o sistema para que o mesmo avise que determinado funcionário possui estabilidade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Existem duas opções  para que o sistema avise que determinado funcionário possui estabilidade. Assim, o usuário poderá escolher uma das 2 opções, conforme contemplar o que deseja. Segue:

* **Opção 1 - Impedimento da Rescisão**

1. Acesse: **Administração de Pessoal | Sindicatos | edite o sindicato desejado | aba Identificação | campo Fórmula de Estabilidade.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27165854689943)

Essa 1ª opção, será utilizada na rescisão, **impedindo** o cadastramento da rescisão quando o resultado da fórmula é verdadeiro.  
  
Exemplo de fórmula para membro CIPA, conforme documentação [CIPA:](https://tdn.totvs.com/display/public/LRM/CIPA)  
  
**SE TABFUNC('MEMBROCIPA','V') = 1**  
**ENTAO 1**  
**SENAO 0**  
**FIMSE**2. Após realizar o passo 1 e a confirmação da demissão o sistema emitirá a mensagem: **"Este funcionário possuem estabilidade garantida segundo a fórmula cadastrada no sindicato XXX ".**XXX = será o código do sindicato.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411606131863)

![](https://totvssuporte.zendesk.com/attachments/token/ASmsCGmFYj6Lc1lCwxLUW1esh/?name=inline-1620697883.png)

* **Opção 2 - Não impedimento da rescisão**

1. Caso deseje que a fórmula seja apenas aviso **(não impedindo a rescisão)**, deverá cadastrar em **Configurações | Parametrizador | Rescisão | Cálculo.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27165854693271)

Exemplo de fórmula:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27165854699031)

2. Após realizar o passo 1, a mensagem na tela de rescisão irá ser apresentada, conforme estrutura da fórmula no Parametrizador, mas não impede a rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27165854702103)

**Importante**Devido ao procedimento ser efetuado através de Fórmula e/ou Fórmula de Cálculo, esse canal de suporte não presta esse tipo de atendimento, sendo necessário verificar internamente com sua equipe de TI se é possível realizar a criação das fórmulas necessárias ou viabilizar junto à nossa Equipe de Consultoria, caso seja de seu interesse.  
  
A equipe de Consultoria é uma equipe de atendimento tarifado, diferenciado e com um escopo mais amplo. Os analistas acessam a sua máquina via acesso remoto e tiram dúvidas pontuais.  
  
**Saiba mais**[RH - RM - FOP - Estabilidade: Cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021911492-RH-RM-FOP-Estabilidade-Cadastro)
