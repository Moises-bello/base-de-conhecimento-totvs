---
article_id: 39228722781335
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: 97443823450f8e22639550ec07f5e2d68c34054c7b1fccef6880c5ca93ef1c43
fetched_at: '2026-06-28T22:40:30.990029+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial
  - Extração de relatórios de movimentos contábeis manuais
type: support-article
updated_at: '2026-03-23T14:57:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39228722781335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Contabilidade-Gerencial-Extra%C3%A7%C3%A3o-de-relat%C3%B3rios-de-movimentos-cont%C3%A1beis-manuais
---

A extração de relatórios para análise de movimentos contábeis manuais no TOTVS Protheus (SIGACTB) é feita pela rotina Conciliador Backoffice (CTBA940), que permite exportar dados em planilha Excel. Para incluir o campo de lançamento manual (CT2\_MANUAL), deve-se configurar a rotina via opção Setup, adicionando esse campo na conciliação personalizada. Após aplicar filtros, os dados podem ser exportados e filtrados para análise detalhada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39228714469911) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
Como realizar a extração de relatórios para análise dos movimentos contábeis lançados manualmente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - Versão 12.1.2210  
  
**Solução**  
Para a extração dessas informações, a rotina padrão indicada é o **Conciliador Backoffice (CTBA940)**.

Esta rotina possui a opção de **Exportar Dados**, que demonstra as informações tanto da origem quanto do destino em formato de planilha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39228714470935)

Dessa forma, é possível exportar, visualizar e filtrar os registros (manuais e automáticos) da maneira desejada.  
  
Formato Exportado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39228722772247)

Por padrão o campo identificador do tipo de lançamento Lcto Manual (`CT2_MANUAL`) não é apresentado nativamente na visão, porem é possível criar um processo de conciliação personalizado através da opção **Setup** da própria rotina, incluindo os campos específicos do lançamento que se deseja disponibilizar para exportação.

Para incluir o campo de Lançamento Manual na exportação do Conciliador, siga o procedimento abaixo:

1. Acesse o módulo de **Contabilidade Gerencial** e abra a rotina **Conciliador** (CTBA940).
2. Na tela inicial do Conciliador, clique na opção **Setup** para gerenciar os arquivos de configurações.
3. Selecione uma configuração existente que atenda à sua base de dados (ex: *"003 - Cópia de Itens das NF de Entrada x Contabilidade"*) e utilize a opção de copiar a configuração ou clique em **Incluir Nova Configuração**.
4. Siga até a etapa de definição de **Campos**. Na área correspondente à tabela de destino (CT2 - Lançamentos Contábeis), pesquise e inclua o campo `CT2_MANUAL` (Lcto Manual).
5. Avance pelas etapas seguintes de *Filtros*, *Amarração* e *Totais*, mantendo as regras desejadas, e clique em **Confirmar Configuração**.
6. Retorne à tela principal do Conciliador e selecione a configuração recém-ajustada no campo de **Configuração de Conciliação**.
7. Preencha os **Filtros** de datas (Ex: *Data Lcto de* e *Data Lcto até*) e demais parâmetros necessários da sua busca, e clique na opção para aplicar.
8. Após o carregamento dos registros na aba de conciliação em tela, clique no botão superior **Exportar Dados**.
9. Salve a planilha gerada em formato Excel (`.xlsx`) em seu computador.
10. Abra a planilha exportada e localize a coluna referente ao Lançamento Manual (geralmente nomeada como `lcto manual` ou `CT2_MANUAL`). Utilize os filtros padrão do próprio Excel para separar os dados (onde, por padrão, '1' representa lançamentos automáticos e '2' os manuais) e realizar a análise de cada relatório.

**Saiba mais:**  
[Setup - Conciliador - CTBA940](https://tdn.totvs.com.br/display/public/PROT/Setup+-+Conciliador+-+CTBA940+-+Contabilidade+Gerencial+-+P12)  
[Conciliador Backoffice - CTBA940](https://tdn.totvs.com.br/display/public/PROT/Conciliador+Backoffice+-+CTBA940+-+P12+-+Contabilidade+Gerencial)  
[Conciliador Protheus - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)  
[SIGACTB- CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-BackOffice)
