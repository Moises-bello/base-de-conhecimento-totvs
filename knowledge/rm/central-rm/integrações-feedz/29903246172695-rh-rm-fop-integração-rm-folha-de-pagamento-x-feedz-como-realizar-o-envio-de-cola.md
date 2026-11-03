---
article_id: 29903246172695
category: Integrações - Feedz
content_hash: 95fe1b086ce3485a6a10d14233bd164a585a81586867dce05ea5b4840bed9c35
fetched_at: '2026-06-28T22:46:41.470413+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como realizar o
  envio de colaboradores e associação de líderes
type: support-article
updated_at: '2025-02-12T12:15:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29903246172695-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-realizar-o-envio-de-colaboradores-e-associa%C3%A7%C3%A3o-de-l%C3%ADderes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29903246140823) Tempo aproximado para leitura: **00:04:55 min** **Dúvida**Como realizar o envio de colaboradores e associação de líderes do RM para a Feedz através da integração?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Solução**A integração de colaboradores do RM para a Feedz, é realizado através da execução da rotina **TOTVS RH Performance e Metas / Feedz** localizada módulo **Folha de pagamento > Administração de Pessoal**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29903612342935)

#### **Envio de Funcionários:**

1. Deverá ser executado a integração, selecionando apenas a opção "**Enviar Funcionários / Cadastros Auxiliares**". Poderá utilizar filtros de seleção para definir quais funcionários serão enviados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29904508121239)

2. Selecione as Coligadas que serão enviadas, marque apenas as que estão parametrizadas para utilizar a integração com Feedz.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29904508122647)

3. Avance para executar, ao finalizar será apresentado os logs informando o resultado da execução:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29904508124695)

4. Se a execução for bem-sucedida, os colaboradores enviados já estarão disponíveis na Feedz.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29907828942359)

#### **Associação de Líderes:**

1. Para vincular o gestor aos colaboradores, execute novamente a rotina de integração, selecionando a opção "**Fazer associação de Líderes**". Poderá marcar também a opção "**Prioriza chefe master no envio**", caso deseje que os chefes master sejam priorizados na associação.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29904483666583)

2. Após execução, será apresentado os logs do resultado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29904508130327)

3. Se a execução for bem-sucedida, o chefe estará vinculado ao colaborador no Feedz:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29904483670807)

**Observações importantes:**

* É importante executar primeiro apenas o **Envio de funcionários** e somente depois a **Associação de líderes,** pois caso o cadastro do gestor ainda não esteja disponível na Feedz, ocorrerá um erro ao tentar realizar a associação.
* Poderá ocorrer alguns erros durante a execução da integração, todos os códigos estão mapeados e para saber como corrigi-los, consulte: [Erro na integração com a Feedz código XXXX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX)
* Na **Associação de Líderes**, o sistema irá associar o chefe direto do subordinado (Hierarquia por posição ou cadastro de chefes/supervisores). Para conhecer a regra de como é definido o chefe direto, quando existe mais de um chefe na mesma seção, consulte: [Explicação do conceito de subordinados diretos e indiretos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418577219735-RH-RM-Meu-RH-Explica%C3%A7%C3%A3o-do-conceito-de-subordinados-diretos-e-indiretos)
* A rotina de integração Feedz será executada automaticamente apenas se for realizado a criação do agendamento do processo. A tela de agendamento é a última etapa exibida antes da execução do processo.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29907828942871)  
    
  Para evitar impacto na performance, recomenda-se que o agendamento seja programado para, no máximo, duas vezes ao dia. Para mais informações sobre a configuração, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=270085915)

**Saiba mais:**

**[TDN - Integração RM x FEEDZ](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)**

**[Integração RM Folha de Pagamento x Feedz - Nenhum funcionário atende a seleção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28206773411095-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-Feedz-Nenhum-funcion%C3%A1rio-atende-a-sele%C3%A7%C3%A3o)**

**[Integração RM Folha de Pagamento x Feedz - Erro na integração com a Feedz código XXXX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX)**
