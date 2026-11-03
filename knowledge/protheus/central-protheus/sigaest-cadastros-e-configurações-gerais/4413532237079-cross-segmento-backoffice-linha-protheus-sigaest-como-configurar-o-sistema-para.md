---
article_id: 4413532237079
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: abf226f0741929ea54feda0c21acf2712487bba7bc0ae789977fc9b372cdcf03
fetched_at: '2026-06-28T22:39:08.122770+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como configurar o
  sistema para movimentar lotes vencidos?
type: support-article
updated_at: '2021-11-18T12:16:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413532237079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-sistema-para-movimentar-lotes-vencidos
---

**Dúvida**

Como possibilitar requisitar produtos com lotes vencidos com destino exclusivo para descarte quando o ambiente esta configurado para não permitir o uso de lotes vencidos?

**Ambiente**  
Este campo somente estará disponível no dicionário das releases superiores à 12.1.27 e a funcionalidade esta disponível em todas versões a partir da publicação deste documento técnico.

Nas releases anteriores à 12.1.27 inclusive, o campo deverá ser criado manualmente conforme passos abaixo.

**Solução**

Esta configuração somente tem efeito nas rotinas de movimentações internas(MATA240) ou múltiplas(MATA241).

Para criação do campo F5\_LOTVENC movimentar lotes vencidos siga os passos abaixo:   
  
1 - Com acesso ao módulo configurador (**SIGACFG**), acesse o menu Base de Dados → Dicionário → Bases de Dados

![passo1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413532084375/passo1.jpg)  
  
2 - No menu à esquerda da tela, clique em **Dicionário de Dados**, pesquise pelo *Prefixo* **SF5  
  
![passo_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517085591/passo_2.jpg)**3 - Clique em **editar**, na árvore a esquerda dê um duplo clique em **Tipos de Movimentação**![tipo_de_movimenta__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517106583/tipo_de_movimenta__o.jpg)

4 - Na árvore à esquerda da tela, clique em **Campos**, clique em Incluir  
![Campos.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517121047/Campos.jpg)

5 - Preencha nos campos **Campo**, **Tipo**,**Tamanho**e **Formato os seguintes valores**F5\_LOTVENC, 1 - Caracter  
![Editar_campo_F5_LOTVENC.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517126039/Editar_campo_F5_LOTVENC.jpg)

6 - Clique na aba **Informações**, preenchendo os seguintes campos **Título** e **Descrição** com os seguinte  valor : Lote Vencido  
![informa__es_titulo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517127959/informa__es_titulo.jpg)

7- Clique na aba **Opções**, preenchendo os seguintes campos : Lista opções = 1=Sim;2=Nao e Inic. Padrão = "2" e clique em salvar

![Op__es.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413508794647/Op__es.jpg)

8 - Após salvar clique no **Check Mark** verde para confirmar 

![confirmar.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517132823/confirmar.jpg)

9 - E na sequencia clique no disquete para atualizar a base de dados  
![Salvar.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517137303/Salvar.jpg)

10 - Confirme a atualização de dados nas próximas telas  
  
![Atualiza__o_de_dados.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413508823319/Atualiza__o_de_dados.jpg)

![Atualiza__o_de_dados_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4413532179607/Atualiza__o_de_dados_2.jpg)

Após Conclusão o campo estará disponível no **cadastro de Tipos de movimentos** na aba outros.   
![Aba_Outros.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413517156119/Aba_Outros.png)

**Observações:**

- Este campo (F5\_LOTVENC) somente estará disponível no dicionário das releases superiores à 12.1.27;

- Nas releases anteriores à 12.1.27  o campo deverá ser criado manualmente conforme passos citados no artigo.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
