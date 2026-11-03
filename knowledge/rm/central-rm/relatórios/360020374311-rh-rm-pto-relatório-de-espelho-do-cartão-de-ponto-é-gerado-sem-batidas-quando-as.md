---
article_id: 360020374311
category: Relatórios
content_hash: eb7c3b77c882495754ac127bf52247329281848fdfd90c0420c55e3a0d0bab2e
fetched_at: '2026-06-28T22:46:39.307780+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: RH - RM - PTO - Relatório de espelho do cartão de ponto é gerado sem batidas
  quando as datas de seleção são de um período anterior
type: support-article
updated_at: '2025-10-15T17:57:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020374311-RH-RM-PTO-Relat%C3%B3rio-de-espelho-do-cart%C3%A3o-de-ponto-%C3%A9-gerado-sem-batidas-quando-as-datas-de-sele%C3%A7%C3%A3o-s%C3%A3o-de-um-per%C3%ADodo-anterior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503072215191) Tempo aproximado para leitura: 00:01:30 min**

**Ocorrência**No módulo **Automação de Ponto**, ao tentar gerar o **Relatório de Espelho do Cartão** para períodos anteriores, este é gerado sem informações as batidas (vazio).   
Obs.: Este cenário também pode ocorrer ao consultar a visão do espelho de ponto no período desejado.     
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144075186199)  
  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre, pois o período selecionado para a geração está em arquivo morto.  
  
**Solução**Para gerar o **R****elatório de Espelho do Cartão** para períodos em arquivo morto, siga os passos abaixo.

1. No módulo de **Automação de Ponto**, acesse o menu **Configurações** | **Períodos**.  
   Selecione o período anterior que está no qual deseja gerar o relatório.  
   Obs.: Confira a coluna Arquivo Morto e caso a caixa de seleção da coluna estiver marcada, indica que os registros estão em arquivo morto.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059566487)
2. Acesse a opção **Processos** | **Transferir dados para as tabelas de produção.** Vai ser aberta a janela de execução.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059567255)
3. Nesta tela está disponível a opção de seleção de funcionários possibilitando realizar o processo parcialmente visando otimizar o tempo de execução do processo. Ao realizar o registro somente para um funcionário ou grupo de funcionários. A caixa de seleção da coluna arquivo morto irá ficar com um quadradinho indicado que há registros movimentados parcialmente:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059569303)
4. Para conferir os funcionários que os registros foram levados para tabela de produção, selecione o período desejado e acesse a opção **Anexos** | **Período do Funcionário:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144075191959)
5. Caso o parâmetro **“Transferir registros para tabela de produção de todos os funcionários”** seja marcado, o filtro realizado na seleção de funcionário será desprezado, e o processo irá realizar a transferência de todos os registros referente ao período selecionado para a tabela de produção sem restrição de funcionários.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059571607)  
     
   Obs.: A caixa de seleção da coluna arquivo morto irá ficar vazia indicado que há registros movimentados parcialmente: ⁣![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059573271)
6. Após fazer a seleção desejada clique no botão executar, para que o processo seja realizado. Ao finalizar o processo basta gerar o relatório novamente.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059574807)
7. Para retornar com os dados para as tabelas de **arquivo morto**, selecione o período e vá em **Processos** | **Transferir dados para as tabelas de arquivo morto**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30144059575703)

**Saiba mais**[T](https://tdn.totvs.com/pages/viewpage.action?pageId=185731949)[ransferir dados para tabela de](https://tdn.totvs.com/pages/viewpage.action?pageId=185731949) [produção: passos](https://tdn.totvs.com/pages/viewpage.action?pageId=185731949)  
[Transferir dados para tabelas de produção: conceito](https://tdn.totvs.com/pages/viewpage.action?pageId=452720003)
