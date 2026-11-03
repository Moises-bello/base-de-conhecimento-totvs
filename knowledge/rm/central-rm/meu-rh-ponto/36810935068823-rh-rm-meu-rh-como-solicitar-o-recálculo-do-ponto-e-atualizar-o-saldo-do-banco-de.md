---
article_id: 36810935068823
category: Meu RH - Ponto
content_hash: 8e415b878aaf843c6fe1875697fff22857d689eb578832bbd34d08c26e06fd99
fetched_at: '2026-06-28T22:47:30.249031+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como solicitar o Recálculo do Ponto e atualizar o saldo
  do banco de horas
type: support-article
updated_at: '2025-12-19T19:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36810935068823-RH-RM-Meu-RH-Como-solicitar-o-Rec%C3%A1lculo-do-Ponto-e-atualizar-o-saldo-do-banco-de-horas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36810949445783) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como solicitar o Recálculo de Ponto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2502.137  
  
**Solução**  
Esta funcionalidade permite o recálculo das marcações de ponto do colaborador, atualizando a apuração do espelho de ponto com base nas alterações realizadas, como inclusão, exclusão ou ajuste de batidas.

Após realizar alterações nas marcações de ponto (como incluir, editar ou excluir batidas), é necessário executar o recálculo para que os dados do espelho de ponto e também do banco de horas sejam atualizados corretamente.

Ao clicar no botão **"Recalcular"**, o sistema processará novamente as marcações do colaborador e atualizará as ocorrências e totalizadores da jornada, de acordo com as regras e parametrizações vigentes no sistema.

### **Situações comuns que exigem o recálculo no período de ponto:**

* Inclusão/aprovação manual de batidas;
* Ajuste de batidas manuais incorretas;
* Solicitação/Aprovação de abono;
* Solicitação de atestado médico;
* Ajuste de atitude das ocorrências de extras, atrasos e faltas;
* Solicitação de sobreaviso.

### **Processo de solicitação do recálculo:**

Ao realizar a solicitação de recálculo, o usuário receberá algumas mensagens informando a ele que o recálculo foi solicitado e que está em andamento. Além disso, abaixo do botão de recálculo será exibida a mensagem: Recálculo em andamento...

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36810935041687)

Após o processo ser concluído com sucesso, na tela será informada a data de execução do recálculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36810935043991)

Caso o job do recálculo finalizar com algum erro, será exibida a mensagem: Falha no recálculo. Tente novamente ou contate o RH para assistência.

Caso o processo de recálculo for finalizado com algum warning, será exibida a mensagem: Confira seu espelho de ponto. Se houver divergência, solicite um novo recálculo ou entre em contato com o RH.

A tabela que guarda os registros de recálculo do Meu RH é a ARECALCULOFUNCMEURH;

É necessário que tanto a versão quando o banco de dados esteja atualizado, desta forma será preciso executar o RM-Atualizador para utilizar a funcionalidade.

Para liberar permissões de recálculo, clique [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36807411169047/live_preview/01KBQV4CSJW9AP6WZQY4ACTBEF).

Mais informações na documentação: [Recálculo do ponto](https://tdn.totvs.com/pages/viewpage.action?pageId=932348278).
