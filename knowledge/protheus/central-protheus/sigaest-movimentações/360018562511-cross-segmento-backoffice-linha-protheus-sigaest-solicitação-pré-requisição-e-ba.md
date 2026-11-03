---
article_id: 360018562511
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5cf0bebfe7ae0bf422b735a0b78cac9a887690eb0fbc94b483a68a1f2fcaacd3
fetched_at: '2026-06-28T22:38:54.171617+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Solicitação, Pré-Requisição
  e Baixa da Pré-Requisição - MATA105 - MATA106 - MATA185
type: support-article
updated_at: '2026-06-18T16:08:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185
---

O artigo explica o processo de Solicitação ao Armazém no Protheus (versão 11.80+), detalhando como realizar a Solicitação (MATA105), gerar a Pré-Requisição (MATA106) e efetuar a Baixa da Pré-Requisição (MATA185). O controle evita desperdícios e exige a baixa para movimentação ou compra. A rotina integra-se via Mensagem Única, sem API própria.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19149375260567)** Tempo aproximado para leitura: **00:03:10 min**

**Dúvida**  
O que é e como realizar a Solicitação, Pré-Requisição e Baixa de estoque pelo processo de Solicitação Armazém

**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A Solicitação ao Armazém é um processo muito usual em muitas empresas, muitas possuem inclusive um setor de controle das Solicitações ao Armazém, para ter um controle se aquela requisição deve ser aprovada mesmo ou não.

Um exemplo genérico: um funcionário precisa de uma caneta para o seu trabalho, efetua uma Solicitação ao Armazém que fica registrada e aguardando a requisição pelo setor ou ao usuário responsável liberar. Então o setor responsável gera a requisição do saldo dessa solicitação e efetua a baixa.

O controle de Solicitação ao Armazém é importante na empresa para prevenir o desperdício de materiais, delegando a um responsável o controle das requisições

Abaixo demonstraremos como efetuar, via *Protheus*, a Solicitação ao Armazém, a Geração da Pré-Requisição e a Baixa da Pré-Requisição:

### **1 - Realizar a inclusão da Solicitação Armazém ( MATA105 )**

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015069831)

### **2 - Acessar a rotina Gera Pré-Requisição selecionar a solicitação ao armazém criada (MATA106)**

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015070251)

Se selecionado o pergunte "Gera Sol.Compras/Atu.Entrega = Sim", sera efetivado a geração da SC (Solicitação de Compras), que podera ser dado continuidade através da rotina MATA110 (Solicitação de Compra).

Caso não desejar gerar a solicitação de compras, e o item possuir saldo zero, sera apresentado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41324410686231)

### **3 - Acessar a rotina Baixa da Pré-Requisição selecionar a pré-requisição criada ( MATA185 )** Sem_t_tulo.png

#### **Resumo do Processo: MATA105 > MATA106 > MATA185**

#### 

**Duvidas possiveis:**

**1) Posso efetuar uma "SA" sem ter o trabalho de gerar uma "Baixa de pre requisição"?**  
R: A Baixa e necessaria para gerar o movimento interno ou a solicitação de compras, então não tem como fazer isso no processo desejado.

**2) A rotina de Solicitação ao Armazém possui API/Integração?**  
R: Ela possui apenas integração via Mensagem Unica (Adapter EAI - Configurador), não tendo API própria.

**3) A rotina de Baixa de Pré-Requisição permite Baixar por Item ou somente pelo Documento Inteiro gerado na Solicitação ao Armazém?**  
R: Ao acessar a rotina BAIXA DA PRE-REQUISIÇÃO (MATA185) perssionar a **Tecla F12** e escolher qual opção deseja Baixar Por: **"Item da Pre-Req."** ou **"Toda a Pre-Req."**.

**4) Gostaria de fazer a baixa de itens de estoque, utilizando um arquivo de excel**  
R: No padrão não existe essa possibilidade.

5) **É possivel incluir uma ordem de produção já encerrada em uma solicitação ao armazém?**

R: Ordens de Produção que **já foram encerradas ou totalmente apontadas** não permitem **alterações nem a inclusão de novas movimentações** no sistema.  
   
Para que seja possível **vincular essa Solicitação ao Armazém**, será necessário **realizar o estorno da Ordem de Produção encerrada**, retornando-a para um status que permita novas movimentações.  
   
Após o estorno, o processo poderá ser executado normalmente conforme o fluxo operacional.

[Manufatura - Linha Protheus - SIGAPCP - Reabrir uma OP que já foi encerrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002187821-Manufatura-Linha-Protheus-SIGAPCP-Reabrir-uma-OP-que-j%C3%A1-foi-encerrada)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Pontos de Entrada da rotina Solicitação ao Armazém*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414520997271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Pontos-de-Entrada-da-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m)
