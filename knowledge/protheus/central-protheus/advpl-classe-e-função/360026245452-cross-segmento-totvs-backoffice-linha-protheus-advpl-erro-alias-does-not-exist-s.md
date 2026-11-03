---
article_id: 360026245452
category: ADVPL - Classe e Função
content_hash: 9591c6618c1d9f5e0341ebaafb168a41cb171b94f5d0f443cdb40ad59eff306c
fetched_at: '2026-06-28T22:40:15.848131+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: alias does
  not exist SM0'
type: support-article
updated_at: '2024-06-03T12:15:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026245452-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-alias-does-not-exist-SM0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23602450226583)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao utilizar alguma de manipulação de banco de dados (especialmente DbCloseArea() e DbUseArea()), o erro "*alias does not exist SM0*" passa a ser apresentado na customização.  
  
**Ambiente**  
Cross Segmento - TOTVS *Backoffice* (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Este erro ocorre porque alguma função, classe ou pseudocomando efetuou o fechamento do arquivo de trabalho SM0.  
  
**Solução**

1. Identificar qual função está ocasionando o fechamento do arquivo:  
   * Insira um ponto de parada no início da sua customização e valide qual função está efetuando o fechamento do arquivo;
   * Funções como DbUseArea() (vide parâmetro lNewArea) e DbCloseArea() podem direta ou indiretamente fechar este arquivo de trabalho.
2. Verificar se já existe uma função/classe que realize a mesma ação sem realizar o fechamento do arquivo temporário:
   * Por exemplo, para manipulação de tabelas temporárias ou arquivos de trabalho, pode ser utilizada a classe FwTemporaryTable().
3. Armazenar e restaurar o estado de um arquivo de trabalho:
   * No início do fonte armazene os arquivos desejados por meio da função GetArea() e restaure ao final das manipulações com a função RestArea().

**Saiba mais**[DBUseArea - Criação de arquivos de trabalho](http://tdn.totvs.com/display/tec/DBUseArea)  
[FWTemporaryTable - Criação de tabelas temporárias](http://tdn.totvs.com/display/framework/FWTemporaryTable)  
[GetArea - Retorna área de trabalho](http://tdn.totvs.com/pages/releaseview.action?pageId=6814876)  
[RestArea - Restauração da área de trabalho](http://tdn.totvs.com/pages/releaseview.action?pageId=6814881)
