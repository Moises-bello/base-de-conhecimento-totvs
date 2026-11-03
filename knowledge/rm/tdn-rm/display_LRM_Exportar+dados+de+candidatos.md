---
content_hash: 56a40cb18af6df5b39aec69946f017b83ba67d2bcf28724015e31c740fc44b71
fetched_at: '2026-06-29T00:09:29.767539+00:00'
page_id: '425458263'
product: rm
source: tdn-rm
title: Exportar dados de candidatos
type: documentation
url: https://tdn.totvs.com/display/LRM/Exportar+dados+de+candidatos
version: 2
---

Através desse processo poderá ser criado um arquivo TXT com os dados necessários do candidato para enviar para a gráfica e montar os cadernos de prova.

Ao executar o processo será necessário escolher o caminho do arquivo onde será criado e poderá adicionar os campos opcionais que serão apresentados neste processo para ser ou não inclusos no arquivo.

Depois deverá escolher para qual etapa deseja gerar o arquivo de exportação. Em seguida serão listadas todas as áreas ofertadas que possuem a etapa selecionada. As áreas que terão caderno de prova incluídos nos arquivos deverão ser marcadas.

**Regra**: Como o intuito principal é que este arquivo seja utilizado na confecção de cadernos para candidatos que ainda irão fazer prova, serão incluídos no arquivo os inscritos para seleção e classificados para próxima etapa, considerando:

* Se for exportação de dados da 1ª Etapa, serão exportados os candidatos com status da 1ª opção (área de interesse) igual a "Inscrito para seleção".

* Se for exportação de dados para etapas após a 1ª, serão exportados os candidatos com status na 1ª Opção (área de interesse) igual a "Classificado para próxima etapa".  Este processo é baseado no seguinte layout: Arquivo de exportação de dados de candidatos para gráfica

Exemplo de uma linha do arquivo txt gerado através do processo de exportação:  
 CODCOLIGADA;IDPS;IDETAPA;NUMERO\_CARTAO;NUMERO\_INSCRICAO;NOME;RG;LINGUA\_ESTRANGEIRA;SALA;PRIMEIRA\_OPCAO;TURNO\_PRIMEIRA\_OPCAO 1;28;37;;13;CARLOS VICENTINO MORAES;;;2º Andar - Sala 01;Ciência da Computação;

Para os campos não preenchidos nos dados do candidato serão exportados vazios separados por ponto e vírgula.
