---
article_id: 23034167955223
category: eSocial - Parametrizador
content_hash: c0f8bbfbaab6e28a9462c0ba7ae5b9ee6b4137769682da8f5e5181f4b4d0380e
fetched_at: '2026-06-28T22:47:06.250369+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Folha Pagamento RM x Outros Backoffices (Autônomos)
  - Tratar dados dos Dependentes
type: support-article
updated_at: '2026-05-27T21:11:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23034167955223-RH-RM-FOP-eSocial-Folha-Pagamento-RM-x-Outros-Backoffices-Aut%C3%B4nomos-Tratar-dados-dos-Dependentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23034161089815) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual evolução foi aplicado no RM, para integração de autônomos com Backoffice Protheus para atender ao Leiaute S-1.2 do eSocial com as informações de dependentes?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da release 12.1.23  
  
**Solução**

Implementado os novos campos na tabela PPAGTOAUTONOMOEXTDEPEND que trata das informações de deduções de dependentes.

Foi liberado uma nova versão da mensageria 1.007 contendo as informações da nova tabela PPAGTOAUTONOMOEXTDEPEND.

Para adequar o produto a nova funcionalidade, siga os passos abaixo. 

1º Após aplicar a versão, será necessário executar os script's de adequação da tabela e dos campos do sistema através do sistema [RM.Atualizador.exe.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687-RH-RM-FOP-RM-Atualizador)

![](https://tdn.totvs.com/download/attachments/817639163/image-2023-12-28_20-45-3.png?version=1&modificationDate=1703807770703&api=v2)

2º Para obter a nova versão, é necessário executar a configuração em **RM**| **Integração | Ferramentas | Configurar**. Essa ação garantirá que a versão mais recente, que inclui as implementações na tabela PPAGTOAUTONOMOEXTDEPEND, seja devidamente atualizada e esteja disponível para utilização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034161092119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034167935639)

3º Após executar o passo 2, acesse **Integração | Integração | Mensagem única | Integrações**, edite a sua integração e cadastre o novo mapeamento. Concluídos esses passos, basta realizar a integração com o Protheus utilizando a nova versão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034161098391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034167939607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034161100183)
