---
article_id: 1500000612621
category: RH - Integração de Titulo
content_hash: 5f5f9d2eec6d388b42682664c1c4d0dcf9c6600ceab3419ce53078022cfd0bf2
fetched_at: '2026-06-28T22:43:36.498477+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar e conferir um título da 2ª Parcela
  do 13º Salário
type: support-article
updated_at: '2025-07-25T19:59:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000612621-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-da-2%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33723836697623) Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como configurar e conferir um título da 2ª Parcela do 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1) Acesse Miscelânea -> Títulos -> Definição:  
![10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33723836699031)

2) Preencha os campos da definição de título:  
**Atenção:** os campos preenchidos no exemplo abaixo são meramente ilustrativos.   
![DEFINI__O_1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000725422)  
  
3) No canto inferior direito, clique em "Definir título" para selecionar a verba e a tabela para busca da informação:   
![DEFINI__O_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360099617454)  
  
4)  Na definição de título, especifique a verba para geração (**verba Líquido 2ª Parcela do 13º Salário = ID 0021**) e a tabela para busca dos valores. No exemplo abaixo, apresentamos a verba de ID 0021 e a busca na tabela **SRD- Histórico de Movimentos**, uma vez que o roteiro 132 foi fechado:  
![definido_pelo_titulo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000760221)  
É importante que a verba selecionada esteja parametrizada como **Base Provento** no campo **Tipo do Cod (RV\_TIPOCOD)** da rotina **Cadastro de Verbas - GPEA040**Acesse: Atualizações -> Definições de Cálculo -> Verbas: efetue a busca pelo identificado no item 4 e faça a validação do conteúdo do campo.

5) Neste grid ainda é possível definir a data de vencimento do título automaticamente, mantendo a mesma tabela para busca da data de vencimento.

Acesse: Outras Ações -> Informações para busca data de vencimento.

![defnido_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000727362)

6) Após a criação do título, verificar no resumo da **2ª Parcela do 13º Salário (Roteiro 132)**, os valores calculados referentes à verba indicada na definição de título:   
Acesse: Relatórios -> Periódicos -> Folha de Pagamento

Processo 00001  
![relatorio_00001.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000729562)

Processo 00005

![relatorio_00005.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360101833213)

7) Acesse Miscelânea -> Títulos -> Geração, configurando os campos de acordo com a definição de título e datas de geração.  
  
8) Verifique na manutenção de títulos, o título gerado com o valor de acordo com o resumo da **2ª Parcela do 13º Salário**:  
Acesse: Miscelânea ->títulos -> Manutenção:  
![titulo_manuten__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000729602)  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
