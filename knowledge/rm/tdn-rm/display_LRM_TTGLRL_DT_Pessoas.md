---
content_hash: c228300f2d25f6c42aa80b58a9172c4a47c4b345995db79f0c9b15433e079892
fetched_at: '2026-06-29T00:06:10.501210+00:00'
page_id: '203763530'
product: rm
source: tdn-rm
title: TTGLRL_DT_Pessoas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGLRL_DT_Pessoas
version: 1
---

# PESSOAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Pessoas* |
| **Situação/Requisito:** | *Ao fazer qualquer alteração na tela que contenha o componente RhuPessoaucObito e tentar salvar dá o seguinte erro:*  *Code generation for property 'PessoaServicos' failed. Error was: 'Property accessor 'PessoaServicos' on object 'rhuPessoaUcObito1' threw the following exception:'Não foi encontrado um servidor ativo nas seguintes configurações:*  *- Protocolo: TCP* *Favor verificar se arquivos de configuração do Servidor e Cliente estão corretos.''* |
| **Solução/Implementação:** | *Otimização no UserControl RhuPessoaucObito, para permitir a edição no DesignMode.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGLRL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
