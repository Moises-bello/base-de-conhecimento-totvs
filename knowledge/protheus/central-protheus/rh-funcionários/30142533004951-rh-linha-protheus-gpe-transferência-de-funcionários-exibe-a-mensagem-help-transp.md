---
article_id: 30142533004951
category: RH - Funcionários
content_hash: 4087203da27d1876721686c482af49f98427b90279cbd250df55777d7d0d7588
fetched_at: '2026-06-28T22:43:28.719748+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: 'RH - Linha Protheus - GPE - Transferência de Funcionários exibe a mensagem
  HELP: TRANSPROC - Período inválido para esse processo'
type: support-article
updated_at: '2025-02-28T13:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30142533004951-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-Funcion%C3%A1rios-exibe-a-mensagem-HELP-TRANSPROC-Per%C3%ADodo-inv%C3%A1lido-para-esse-processo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30142490085399) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Ao realizar a transferência de um Funcionário entre Filias/Empresas, é demonstrada a mensagem ***HELP*: TRANSPROC** **- Período inválido para esse processo**, impossibilitando a conclusão da transferência.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Foram implementados ajustes na rotina de Transferência, em relação às mensagens abaixo:  
**-> Período Inválido**  
**-> Período Superior**  
**-> Período Aberto**

Durante a Transferência de Empresas/Filial/Processo, a rotina passa a exibir a tela abaixo com os **registros dos movimentos** do Funcionário que foram encontrados, além de mensagem explicativa sobre essa etapa.  
**OBS:** Caso o Período/Número de Pagamento ativo no Destino seja **idêntico** ao Período/Número de Pagamento do movimento e ele estiver **ativo**, essas informações são retornadas em tela como sugestão ao usuário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30205843181463)

**-> Período Inválido**Neste caso, será validado se o período informado é **válido**, ou seja, **se existe no destino,** caso contrário a transferência não poderá ser processada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30205852147351)

**-> Período Superior**Neste caso, será validado se os **períodos ativos** nas Empresas/Filiais de origem/destino **são iguais.**  
  
A transferência **não poderá ser efetivada**, se tivermos o cenário de exemplo abaixo:• Empresa 01 (origem) - **Período 10/2024 aberto**  
• Empresa 02 (destino) - **Período 07/2024 aberto**  
• Transferência processada em 10/2024, ou seja, **o período ativo da Empresa origem é superior ao período ativo da Empresa destino**, portanto, a transferência não pode ser executada enquanto o período 10/2024 não estiver ativo na Empresa 02 (destino).

![image-2025-2-11_9-21-32.png](https://tdn.totvs.com/download/attachments/913802247/image-2025-2-11_9-21-32.png?version=1&modificationDate=1739276829223&api=v2)

**-> Período Aberto**  
Neste caso, será validado se o **Período/Número de Pagamento** do destino selecionado está **aberto,** caso contrário, a transferência não poderá ser processada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30205843187351)

Para ter acesso a essa manutenção, é necessário aplicar o pacote de [Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO), com data superior ao dia 18.02.2025.

**Saiba mais:**[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=913802247)  
[Manual - Transferência](https://tdn.totvs.com/pages/viewpage.action?pageId=815569538)  
[RH - Linha Protheus - GPE - Funcionamento do parâmetro MV\_ARQTRAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013366292-RH-Linha-Protheus-GPE-Funcionamento-do-par%C3%A2metro-MV-ARQTRAN)  
[RH - Linha Protheus - GPE - Modo de compartilhamento correto para efetivação de transferência de funcionários entre empresas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060368253-RH-Linha-Protheus-GPE-Modo-de-compartilhamento-correto-para-efetiva%C3%A7%C3%A3o-de-transfer%C3%AAncia-de-funcion%C3%A1rios-entre-empresas)
