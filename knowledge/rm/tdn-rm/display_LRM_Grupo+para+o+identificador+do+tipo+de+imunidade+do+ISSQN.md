---
content_hash: 7106cedeec1569aef3fa2c130e5eb7e105f03153fe829d2de6e77b9b242c92f8
fetched_at: '2026-06-29T00:05:52.093513+00:00'
page_id: '1056144786'
product: rm
source: tdn-rm
title: Grupo para o identificador do tipo de imunidade do ISSQN
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+para+o+identificador+do+tipo+de+imunidade+do+ISSQN
version: 2
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| tribMun | [valores](https://tdn.totvs.com/pages/viewpage.action?pageId=560653837) | G | 1-1 | Grupo para o identificador do tipo de imunidade do ISSQN. |  |  |
| tpImunidade | tribMun | E | 0-1 | Identificação da Imunidade do ISSQN. Somente para o caso de Imunidade. | DFILIAL.TIPOIMUNIDADE | Gerado quando o Regime Tributário da filial for igual a Imune e o tipo de imunidade (disponível em Filial > Anexos > Dados Fiscais, conforme [documentação](https://tdn.totvs.com/display/public/LRM/Dados+Fiscais#1-1563551098)) estiver preenchido.  0 - Imunidade (tipo não informado na nota de origem); 1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a); 2 - Templos de qualquer culto (CF88, Art 150, VI, b); 3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das     entidades sindicais dos trabalhadores, das instituições de educação e de assistência     social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c); 4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d); 5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras     musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por     artistas brasileiros bem como os suportes materiais ou arquivos digitais que os     contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.     (CF88, Art 150, VI, e); |
