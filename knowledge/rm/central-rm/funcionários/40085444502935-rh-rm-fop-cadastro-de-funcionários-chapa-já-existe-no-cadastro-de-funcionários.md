---
article_id: 40085444502935
category: Funcionários
content_hash: 7c3851481f735e13baa7532ad32484053230a286b1241b01195fc32ea4a79d40
fetched_at: '2026-06-28T22:47:03.128022+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Cadastro de Funcionários: Chapa já existe no cadastro de funcionários'
type: support-article
updated_at: '2026-04-30T12:22:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40085444502935-RH-RM-FOP-Cadastro-de-Funcion%C3%A1rios-Chapa-j%C3%A1-existe-no-cadastro-de-funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40085466716055) Tempo aproximado para leitura: 00**:04:45 min**  
  
**Dúvida**  
Como ajustar a sequência de chapas no cadastro de funcionário?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Este erro pode ocorrer quando a sequencia que é armazenada na tabela GAUTOINC está sem sincronização. Quando é utilizada o auto incremento, o RM armazena a última chapa cadastrada e para a nova admissão realiza a conta N + 1.

Para solucionar esse o erro verifique os seguintes passos:

1. Execute as seguintes consultas para verificar o valor de Auto incremento e o valor da Chapa máxima:    
   
select CODCOLIGADA, VALAUTOINC from GAUTOINC  
where CODAUTOINC='CADASTROAUTOMATICOCHAPASSEQUENC'  
and CODSISTEMA='P'  
  
select MAX(chapa) AS CHAPA from PFUNC  
where CODCOLIGADA='informe o código da coligada'

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40095963065367)

2. Para ajustar o controle de chapa sequencial você terá que ajustar o campo VALAUTOINC da tabela GAUTOINC, deixando-o com o mesmo número da sua última chapa cadastrada na PFUNC conforme resultado da sentença SQL (select MAX(pfunc.chapa) from PFUNC).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40095963068951)  
   
**Observação importante:** Lembrando que ao fazer o update terá que passar um filtro para que o campo VALAUTOINC seja alterando somente quando a coluna codautoinc seja igual 'CADASTROAUTOMATICOCHAPASSEQUENC'.

**Importante: Para este ajuste sugerimos acionar o DBA responsável pela base de dados.**  
**Por questões de segurança sugerimos primeiro realizar o procedimento em um ambiente de teste. Após certificar que não ocorreu inconsistência execute na base de produção mediante a backup da base.**

No suporte padrão é para esclarecimento de dúvidas pontuais, logo não desenvolvemos scripts. Caso deseje poderá acionar o serviço de consultoria.

Caso tenha interesse na equipe de Consultoria! É uma equipe de atendimento personalizado capaz de atender o cliente de forma diferenciada, além de contar com um escopo mais amplo. Os analistas atuam diretamente no seu ambiente via acesso remoto.

Contato: 4003-0015

URA: 2-3-3-4-2-2.

Saiba mais:

[RH - RM - FOP - Geração automática de chapa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052721134-RH-RM-FOP-Gera%C3%A7%C3%A3o-autom%C3%A1tica-de-chapa)

[RH - RM - FOP - Configurações de chapa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060623353-RH-RM-FOP-Configura%C3%A7%C3%B5es-de-chapa?source=search)
