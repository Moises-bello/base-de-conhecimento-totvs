---
content_hash: 09faf25e13d3daffdc1d91006b986f984a3ed8851c52b1660166f0112d13d4db
fetched_at: '2026-06-29T00:10:43.695633+00:00'
page_id: '550325853'
product: rm
source: tdn-rm
title: Processo Excluir Inscrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550325853
version: 4
---

Este processo é executado a partir da tela de “Inscrição dos candidatos”. Por meio desse assistente, uma inscrição pode ser excluída independentemente do período em que o Processo Seletivo se encontrar. O processo pode ser executado para uma ou mais inscrições selecionadas a partir da tela.

Para que uma inscrição possa ser excluída, o candidato não poderá ter comparecido às chamadas em nenhuma de suas áreas opcionais.  Após a exclusão, o candidato continuará com a sua conta de usuário e poderá acessar novamente o Portal. As suas inscrições excluídas não serão visualizadas por ele durante os novos acessos.

Ao executar o assistente, a parametrização a ser feita diz respeito à operação (exclusão) que deve ser executada, além de um campo de texto (obrigatório preenchimento) referente ao motivo da exclusão. Os dados de todas as exclusões de inscrição dos diversos candidatos podem ser consultados na tela de “inscrições canceladas/excluídas”. Conforme a ilustração abaixo:

**Exclusão** - Quando uma inscrição for excluída, todas as referências a ela serão completamente removidas do Sistema. Após a exclusão da inscrição se alguma referência não puder ser excluída, a inscrição será mantida inalterada. Veja a seguir as ações que são realizadas durante o processo de exclusão de uma determinada inscrição:

* **Exclusão do lançamento financeiro** - Se a inscrição não tiver originado de uma inscrição anônima e possuir um lançamento financeiro vinculado, ocorrerá a tentativa de exclusão do mesmo. Eventualmente a tentativa de exclusão poderá não ser bem sucedida. Se isso ocorrer, a operação de exclusão da inscrição será interrompida e a inscrição permanecerá inalterada. Essa situação irá ocorrer, por exemplo, se o lançamento financeiro estiver baixado.  Nesse caso, antes de excluir a inscrição, será necessário estornar a baixa do lançamento diretamente no TOTVS Gestão Financeira;
* **Exclusão dos registros que referenciam à inscrição** - Serão excluídos eventuais vínculos com cadernos de provas, alocação, documentos, histórico de formas de inscrição, opções de idiomas, presença, atividades agendadas, arquivos enviados pelo candidato e histórico de classificação;
* **Exclusão do registro de inscrição** - Após a remoção de todos os registros vinculados, o registro da inscrição será excluído;

Ao final, o Sistema apresentará as exclusões que foram realizadas e as que não foram por algum motivo.
