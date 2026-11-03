---
content_hash: 89127cfcf7a3c2012ae3cc60cd5d0479556b1039b9e998d41f8a91eb134886d5
fetched_at: '2026-06-29T00:11:55.942998+00:00'
page_id: '864986537'
product: rm
source: tdn-rm
title: Enviar Apontamentos para o Manutenção de Ativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864986537
version: 3
---

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Mobilidade \ Equipamentos \ Apontamentos de Equipamentos \ Processos \ Enviar apontamentos para o Manutenção de Ativos;
* O parâmetro “Integrado com o SIGA-MNT” deve estar HABILITADO;
* Este processo é responsável por enviar ao SIGA-MNT apontamentos de equipamentos provenientes dos coletores móveis. Este envio será através de mensagem única e pode ser acionado de duas formas: manualmente ou automaticamente;
* Primeiramente, logo após salvar os apontamentos originados de um coletor, uma rotina automática é disparada consolidando os dados de apontamentos em um XML no formato da mensagem única que será enviado ao SIGA-MNT;
* Como podem ocorrer erros na geração automática da mensagem, o sistema permitirá que a rotina seja disparada manualmente através do processo “Enviar Apontamentos para o Manutenção de Ativos”. O usuário deverá selecionar quais registros serão enviados e acionar o processo;
* Apenas registros com status “Pendente” serão considerados. Caso algum registro possua status diferente, o sistema deverá emitir um alerta ao usuário com uma mensagem explicativa, mas não impedirá a execução do processo. Após o término do envio, o status dos apontamentos será alterado para “Enviado”;
* As seguintes informações são enviadas para o SIGA-MNT:
  + Código da Coligada;
  + Filial do Projeto;
  + Código de Barras do Bem;
  + Data/Hora Inicial;
  + Data/Hora Final;
  + Centro de Custo;
  + Código do Motivo de Improdutividade;
  + Horímetro;
  + Tarefa.
* Para que o envio automático seja realizado, deve ser configurada uma fórmula visual;
* A sincronização é feita via Mensagem Única:
  + Código: 1005;
  + Descrição: TOTVS Construção Obras e Projetos x Manutenção de Ativos;

* Mensagem/Versão: APPOINTMENT / 1.000.

[Custos do Período – SIGAMNT](https://tdn.totvs.com/pages/viewpage.action?pageId=864986742)
