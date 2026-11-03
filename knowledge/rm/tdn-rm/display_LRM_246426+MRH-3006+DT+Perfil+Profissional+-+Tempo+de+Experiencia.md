---
content_hash: df163a50b759eae2bb09a66daccaf9388c3f1e2e52f56783b5e051add2e7b02b
fetched_at: '2026-06-29T00:08:28.858197+00:00'
page_id: '271862882'
product: rm
source: tdn-rm
title: 246426 MRH-3006 DT Perfil Profissional - Tempo de Experiencia
type: documentation
url: https://tdn.totvs.com/display/LRM/246426+MRH-3006+DT+Perfil+Profissional+-+Tempo+de+Experiencia
version: 114
---

# RFIL PROFISSIONAL - TEMPO DE EXPERIÊNCIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Rotina:** | |  | | --- | | **Rotina** | | Atualização do Perfil Profissional no currículo. |  |  | | --- | | **Rotina(s) envolvida(s)** | | Atualização do Perfil Profissional no currículo no portal Banco de Talentos. | | Atualização do Perfil Profissional no currículo no RM.exe. | | Atualização da impressão do currículo no portal Banco de Talentos. | | Alteração do conceito das colunas 'TEMPOEXPPROF', 'EXPERIENCIAAREACURR1', 'EXPERIENCIAAREACURR2', agora ao invés de ser o total de anos, será o total de meses (anos + meses). | |
| **Cadastros Iniciais:** | Para utilização do requisito basta acessar o Perfil Profissional pelo Banco de Talentos, pelo Candidato ou Currículos Externos pelo RM.exe. |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Ponto de Entrada:** | *Informe o ponto de entrada relacionado (link).* |
| **Tickets relacionados** | 246426 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [MRH-3006](http://jiraproducao.totvs.com.br/browse/MRH-3006 "MRH-3006") |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | VCANDIDATOS |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação visa possibilitar inserir quantidade de  meses e anos no Perfil Profissional.

## Importante

Será necessário converter todos os dados que estão em anos, para meses.

| Tabela | Coluna |
| --- | --- |
| VCANDIDATOS | TEMPOEXPPROF |
| VCANDIDATOS | EXPERIENCIAAREACURR1 |
| VCANDIDATOS | EXPERIENCIAAREACURR2 |

O processo é feito multiplicando o valor atual em anos por 12 convertendo em meses.

Para isso foi criado um Script que irá rodar automaticamente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado;

## Procedimento para Utilização

***Banco de Talentos***

* Acesse o Banco de Talentos;
* Entre em Perfil;
* Em Perfil Profissional clique em Editar Perfil Profissional
* Preencha os dados de Experiência profissional total, Experiência na área principal e/ou Experiência na área opcional, pode ser preenchido somente um dos campos caso seja necessário.

* Assim que salvar o ficará da seguinte forma:

* Na impressão do currículo também será visualizado dessa forma:

***RM.exe***

* Acesse o Candidato ou Currículo Externo;
  + Acesso ao Candidato (RH > Gestão de Pessoas > Planejamento e Capitação > Candidatos)
  + Acesso ao Currículo Externo (RH > Gestão de Pessoas > Planejamento e Capitação > Currículos Externos)
  + Abrir o Candidato/Currículo e acessar Perfil Profissional

Para todos os processos o sistema converte automaticamente de meses para anos e meses, para mostrar na tela e após editar de anos e meses para meses e salva no banco.

divs
