---
article_id: 6606176786327
category: Funcionários
content_hash: d267db5a1d8e8574fc94c9b3caa4c34f539401695cd805162282a006b42ee206
fetched_at: '2026-06-28T22:47:03.302385+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Exportação de fotos dos funcionários
type: support-article
updated_at: '2025-03-12T13:44:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6606176786327-RH-RM-FOP-Exporta%C3%A7%C3%A3o-de-fotos-dos-funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:45 min** **Dúvida**Como faço a exportação das fotos dos funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
**Solução**Para exportar a foto do funcionário, acesse Administração de Pessoal | Funcionários, selecione o funcionário desejado e clique em editar. Na aba Identificação localize o símbolo de um disquete acima da foto do funcionário:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6605837449111/mceclip0.png)  
  
Ao clicar neste ícone basta escolher o diretório e atribuir um nome para salvá-la.O sistema não possui uma rotina para exportar as fotos do cadastro do funcionário em lote.  As imagens são levadas para o banco na tabela GIMAGENS na qual não é gravada como extensão de arquivo de imagens.  
  
As tabelas onde são armazenadas as fotos são IDIMAGEM e GIMAGEM. É possível realizar uma consulta SQL para identificar qual imagem pertence a cada funcionário:  
   
SELECT IDIMAGEM,\* FROM PPESSOA   
   
SELECT \* FROM GIMAGEM WHERE ID = XXX   
   
Onde, XXX é a referência da imagem de um determinado funcionário e a coluna código retornada na pesquisa representa o Identificador do funcionário. No exemplo abaixo o id 844 representa a imagem do funcionário cujo identificador é 1:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6606037714327/mceclip1.png)
