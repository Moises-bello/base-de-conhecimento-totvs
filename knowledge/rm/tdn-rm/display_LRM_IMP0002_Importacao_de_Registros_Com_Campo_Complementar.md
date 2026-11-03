---
content_hash: 584750db5d99c1a932a2c22e18634dbd18c790c3dcd81bc1bbb468534c9325e3
fetched_at: '2026-06-29T00:08:19.879232+00:00'
page_id: '267796264'
product: rm
source: tdn-rm
title: IMP0002_Importacao_de_Registros_Com_Campo_Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/IMP0002_Importacao_de_Registros_Com_Campo_Complementar
version: 12
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 12.1.4 e superiores |
| **Ocorrência:** | Importação de Campos Complementares via Conceito |
| **Ambiente:** | Importação |
| **Passo a passo:** | Este documento tem por finalidade ensinar os usuários a importar os campos complementares existentes na base de dados.  Como exemplo, utilizaremos os campos complementares de movimento. Passo a Passo **1 º - Identificar os campos complementares existentes.**  Acessar o módulo Delphi - RMNucleus.exe e ir no menu Utilitários - Importações / Exportações - Importar Arquivos Texto      Será carregada a tela de Importação conforme abaixo:      Seguindo nosso exemplo, deverá selecionar a versão do layout a qual deseja ver seu conteúdo, depois expandir a seleção de cadastros disponíveis e por fim selecionar qual cadastro deseja. Neste caso vamos utilizar a importação de movimento, por tanto foi selecionado o layout 3.0 e clicamos em Movimentos.  A tela abaixo será carregada:    Clique sobre o menu Arquivo, depois Salvar...    Após salvar arquivo, edite-o e procure as Tabelas de Campos Complementares. Tabelas de Campos ComplementaresCampos ComplementaresMovimento  Item de Movimento     Pronto! Realizando este primeiro passo já podemos identificar todos os campos complementares de Item/Movimento existentes na base de dados.    Aconselhamos que para teste, utilize um arquivo de texto válido e exportado pelo sistema para evitar possíveis erros na importação.  A documentação abaixo aborda como obter um arquivo exemplo:      **2º - Edição do arquivo de texto**  De posse do arquivo txt, note que foi gerada a linha O porém sem conteúdo.      Desta forma o que terá que fazer é criar a linha O manualmente conforme layout dos campos obtidos no **Passo 1.**  O arquivo deverá ficar desta forma:    Após criar o mesmo deverá importa-lo utilizando o conceito padrão TOTVS. Não será necessário nenhuma alteração no Conceito.  Como nosso arquivo txt foi obtido a partir de um movimento já existente, no momento de processar o Conceito, deverá ser marcada a opção de Atualizar Movimento Cadastrado.  Pronto! Após término do processo, busque seu movimento editado na base de dados e confira os campos complementares.    Em nosso exemplo, o mesmo ficou desta forma:      Abaixo, segue arquivo txt utilizado como exemplo. Baixe o mesmo e visualize a linha O por completa.  150 |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
