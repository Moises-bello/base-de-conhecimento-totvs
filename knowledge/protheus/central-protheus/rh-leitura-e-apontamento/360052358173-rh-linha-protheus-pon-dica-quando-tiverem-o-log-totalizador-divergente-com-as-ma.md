---
article_id: 360052358173
category: RH - Leitura e Apontamento
content_hash: e62fb7213cb680b51e7c4be9e34143113c745f3cc1c4653eba76c66040c876d0
fetched_at: '2026-06-28T22:44:45.940944+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: 'RH - Linha Protheus - PON - Dica quando tiverem o log: Totalizador divergente
  com as marcações do arquivo txt'
type: support-article
updated_at: '2025-06-13T18:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052358173-RH-Linha-Protheus-PON-Dica-quando-tiverem-o-log-Totalizador-divergente-com-as-marca%C3%A7%C3%B5es-do-arquivo-txt
---

**Dúvida**Dica quando tiverem o log: Totalizador divergente com as marcações do arquivo txt  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
**Solução**Tivemos recentemente, um caso onde no arquivo txt de um cliente, em seu totalizador contabilizava uma marcação a mais do que as que realmente tinham no corpo do arquivo.  
Após diversos testes, descobrimos se tratar de um erro na obtenção e produção do arquivo.txt, onde a primeira marcação do arquivo ([primeiro NSR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068372-MP-PON-Funcionalidade-da-tabela-RFB-e-como-controlar-a-leitura-para-que-o-NSR-n%C3%A3o-ocasione-erros-no-processo)) se encontrava juntamente com o cabeçalho do arquivo (dados da Empresa).  
  
Pelo *layout* do arquivo txt, chancelado pela [Portaria 1510/2009](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016819371-MP-PON-Descri%C3%A7%C3%A3o-dos-campos-no-leiaute-do-arquivo-AFD-Arquivo-de-Fonte-de-Dados-conforme-Portaria-1510-2009), a primeira linha refere-se à Razão Social da Empresa e seu CNPJ, a partir da segunda linha, temos as marcações do arquivo.  
  
Porém, só descobrimos essa divergência quando o arquivo txt, foi aberto pelo Programa do *Windows* Bloco de Notas, pois pelo *Notepad*++ ou *Word*, o arquivo estava correto.  
  
Veja abaixo o arquivo aberto no *Notepad++  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081625854/mceclip1.png)*Note que, na primeira linha o Programa demonstra a marcação de número de NSR 000001258  
  
O totalizador, nesse caso, contabilizou 420 marcações, veja:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081625954/mceclip2.png)  
Porém, quando o arquivo txt era lido no Protheus, trazia o log de Marcações divergentes do totalizador, com isso, acessei o Cadastro do Relógio, posicionando no código deste REP e [cliquei em F4](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016519452-MP-PON-Ap%C3%B3s-o-cadastro-do-rel%C3%B3gio-como-podemos-ter-uma-pr%C3%A9via-se-o-arquivo-ser%C3%A1-lido-pelo-Sistema).  
  
Com isso, o Sistema me trouxe uma totalidade de 419 marcações ( 1 a menos ).  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082767933/mceclip3.png)  
  
Agora, veja quando eu abro este mesmo arquivo.txt no Bloco de Notas:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082768453/mceclip5.png)  
O arquivo me traz o primeiro NSR sendo o 000001259, ou seja, 419 marcações.  
  
Mas onde está a marcação do NSR 000001258?  
A resposta é: Na primeira linha junto com os dados da Empresa no final do arquivo.txt  
*![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082768733/mceclip6.png)*  
  
O Sistema Protheus, lê o arquivo txt "puro", ou seja, sem tabulações ou tratamento que algum Programa tenha, assim, para a Leitura e Apontamento esta primeira linha, estava sendo ignorada, pois não estava no padrão correto (a partir da segunda linha do txt).  
  
Por isso, o Sistema acusou 419 marcações, mas no arquivo txt quando ele foi gerado, o totalizador contabilizou 420.   
  
A solução paliativa foi, posicionar o cursor antes do primeiro 0 do NSR e dar um *ENTER*no teclado para que, essa marcação vá para a linha de baixo.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081631694/mceclip7.png)  
  
Após, o arquivo foi salvo no mesmo formato e nome para importar corretamente as marcações.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081632034/mceclip8.png)
