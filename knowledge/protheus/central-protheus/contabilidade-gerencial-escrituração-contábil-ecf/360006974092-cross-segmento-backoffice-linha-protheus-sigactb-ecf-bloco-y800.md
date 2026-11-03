---
article_id: 360006974092
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 87bc7dc263edb435feb2b1bf626d389fc86aebcbb7e7e62fd868b5383ee8637d
fetched_at: '2026-06-28T22:40:47.324517+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Bloco Y800
type: support-article
updated_at: '2022-06-03T21:20:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006974092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Bloco-Y800
---

**Dúvida**

Procedimento para gerar o bloco Y800.  
   
 **Ambiente**

Protheus  – Contabilidade  – A partir da versão 11.80  
   
**Solução**

* [Registro Y800: Outras Informações: Atualização de texto e inclusão de campos](http://tdn.totvs.com/display/public/PROT/ECF_SPED_CONTABIL_FISCAL_Alteracoes_para_Leiaute_3_00)

O procedimento para anexar é o seguinte no próprio arquivo .txt:

1 – Digite o documento que deseja anexar no *Word*;

2 – Salve o documento como .rtf;

3 – Abra o documento no Bloco de Notas;

4 – Copie todo o conteúdo do arquivo aberto no Bloco de Notas;

5 – Cole o conteúdo copiado no registro Y800;

6 – Importe o arquivo, de acordo com o Leiaute da ECF, para o programa da ECF.

* Funcionalidade de inclusão arquivo cadastrado no Y800 no programa da ECF:

1 – Selecionar a opção incluir arquivo rtf.  
2 – O sistema abre uma interface de localização de arquivo.  
3 – Selecionar somente arquivo ".RTF" (formato RTF)  
4 – O sistema copia o arquivo para a pasta do sistema com o nome padronizado.  
5 – O sistema calcula o *hash* e armazena o nome o local e o *hash* da cópia do arquivo selecionado.   
6 – O sistema coloca o nome do arquivo no campo descrição.

* Funcionalidade de exclusão arquivo cadastrado no Y800 no programa da ECF:

1 – Selecionar um registro e solicitar a exclusão (Botão "-").  
2 – O sistema exclui o registro Y800 e o arquivo na pasta.

É possível ver o arquivo em formato texto *RTF*em Relatório/Outras Informações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007577131/mceclip0.png)

* Verifique se as tabelas e retinas abaixo o Bloco Y800 foi gerado

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

**Error que podem ser ocasionados**

* [MP - SIGACTB - ECF - Erro Descritor Validador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006849812-MP-SIGACTB-ECF-Erro-Descritor-Validador-)
