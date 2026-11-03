---
content_hash: c10e7fe81d38be7ed29883b1ed81b18b0f46a6147ecdc033643780d1760e77eb
fetched_at: '2026-06-29T00:08:03.477633+00:00'
page_id: '235322577'
product: rm
source: tdn-rm
title: NFE0026_Preenchimento_Campo_Consumidor_Final_Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235322577
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | 11.82.42 & 12.1.9 |
| **Ocorrência:** | Preencher o campo Consumidor Final automaticamente no Movimento de NF-E |
| **Ambiente:** | Inclusão de movimento para envio de NF-E |
| **Passo a passo:** | **Importação da Fórmula visual:**   * Fazer o Download do arquivo abaixo:  150   * Realizar a importação da Fórmula visual através do menu:   Gestão | Fórmula Visual | Fórmula Visual | Execute o filtro desejado | Processos | Importação de Fórmula visual.  Na execução do processo será preciso definir para qual coligada o arquivo será gerado...    e informar a categoria associada ao perfil do Usuário e marcar a flag "Importar Gatilhos"...    Após o preenchimento dos campos, clicar em Executar para que o sistema finalize a importação.    A fórmula visual fará o preenchimento do campo "Consumidor Final" Sempre após salvar o movimento e para todos os movimentos que tenham o campo habilitado para edição. Caso seja necessário desmarcar a flag, deverá realizar o "Salvar" do Movimento e logo em seguida editá-lo. Lembrando que existem outras maneiras de tratar o preenchimento do campo no movimento, porém deverá ser tratado como customização de uma nova fórmula visual.    **Importante:**   * Esta fórmula funcionará para os processos:   - Cópia por Referência - Cópia de movimento selecionado - Inclusão direta (incluir) - Faturamento - Faturamento Automático - Inclusão via outros módulos (Ex. Educacional)   * Caso exista a necessidade de filtrar os tipos de movimento que deverão executar a fórmula, deverá utilizar as atividades:   - Grupo de atividade: TOTVS Movimento | Atividade: "Consulta valor no contexto do Movimento(Assinante)" *(movConsultaValorContextSubScriberActivity)*    - Grupo de atividade: Padrão | Atividade: "Se/Senão" *(ifElseActivity)*    A configuração e validação do(s) campo(s) fica a cargo do usuário responsável. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
