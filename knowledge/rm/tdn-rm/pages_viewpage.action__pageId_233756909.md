---
content_hash: 78ba54497e026bc8b646abd66f3ea6ec71d8c05e85cccc42927c1456b77d3475
fetched_at: '2026-06-29T00:06:28.663864+00:00'
page_id: '233756909'
product: rm
source: tdn-rm
title: TIN005_11_Migrar Gráficos, Relatórios e Sentenças SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233756909
version: 4
---

|  |  |
| --- | --- |
| Descrição | MIGRAR GRÁFICOS, RELATÓRIOS E SENTENÇAS SQL DOS CADASTROS ANTIGOS PARA OS NOVOS |
| Observações | Este processo verifica se o cadastro de telas revitalizadas foram atualizadas, para depois atualizar os objetos gerencias (relatórios, gráficos e sql) que possam estar associados as visões (cadastros) antigas.    Ao executar a ultima opção será exibida a tela       * "Atualiza a tabela com informações das actions encontradas no broker": através desta opção a ferramenta verifica as telas que foram alteradas e registram novamente no broker. **O usuário não deve mudar esta opção.** * "Adiciona a tabela actions encontradas no broker": através desta opção a ferramenta verifica se novas telas foram criadas no TIN e registram no broker. **O usuário não deve mudar esta opção.** * "Exclui da tabela actions não encontradas no broker":através desta opção a ferramenta exclui telas que não existe mais do broker. Esta opção só deve ser marcado sob a orientação da equipe de apoio TOTVS que acompanha a conversão.   Ao executar a "Atualização de Actions" a ferramenta, associa todos os objetos gerencias (relatórios, gráficos e sql) as novas telas da versão revitalizada.     Observação **A execução deste processo não é impeditivo para a migração da Revitalização, mas sugerimos para melhoria de performance do sistema.**    Em seguida, será executado o processo que lista todos os objetos gerenciais que utilizam as tabelas "XPARCELAPAGAMENTO" e "XPARCELACOMPONENTE", devido a transformação delas em VIEWS na base de dados, onde deverão ser migrados estas para as referências das tabelas do financeiro "FLAN", FLANINTEGRACAO, FLANBAIXA E FLANBAIXAINTEGRACAO.  Serão listados todos os relatórios, cubos, gráficos, planilhas ou sentenças SQL que referenciem uma dessas tabelas. Da própria visão é possível editar os objetos (exceto relatórios Delphi) ou exportar a lista para posterior verificação.  É importante ressaltar que não foi quebrada a compatibilidade e a alteração desses objetos não é obrigatória mas é altamente recomendada por questões de performance - visões de dados (views) não possuem performance adequada no banco de dados quanto tabelas.        A seguir apresentamos um exemplo de consulta SQL para obter o valor da parcela e respectivo valor baixado utilizando as tabelas do financeiro correspondentes as tabelas "XPARCELAPAGAMENTO" e "XPARCELACOMPONENTE" transformadas em VIEW.       sqlExemplo SQL 0 WHERE FLANINTEGRACAO.CODCOLIGADA = FLAN.CODCOLIGADA AND FLANINTEGRACAO.IDLAN = FLAN.IDLAN)VR\_PARC , (SELECT COALESCE(SUM(FLANBAIXA.VALORBAIXA),0) + COALESCE(SUM(FLANBAIXA.VALORDESCONTO),0) FROM FLANBAIXA (NOLOCK) WHERE FLANBAIXA.CODCOLIGADA = FLAN.CODCOLIGADA AND FLANBAIXA.IDLAN = FLAN.IDLAN AND FLANBAIXA.STATUS <> 1 /\*CANCELADO\*/ )VR\_BAIXADO, FLAN.STATUSLAN FROM XVENDAPARCELA (NOLOCK) JOIN FLAN (NOLOCK) ON FLAN.IDLAN = XVENDAPARCELA.IDLAN AND FLAN.CODCOLIGADA = XVENDAPARCELA.CODCOLIGADA AND FLAN.STATUSLAN <> 2 /\*CANCELADO\*/ WHERE XVENDAPARCELA.NUMVENDA = 1111]]> |
|  |  |
