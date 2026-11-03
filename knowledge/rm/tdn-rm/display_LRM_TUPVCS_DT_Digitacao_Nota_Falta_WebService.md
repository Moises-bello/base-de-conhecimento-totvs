---
content_hash: 5f25d0ccbdc4dab019e0d4e35d1d70f2f747b804c82ab02a3525fdd8af2ecb51
fetched_at: '2026-06-29T00:08:07.599891+00:00'
page_id: '237382793'
product: rm
source: tdn-rm
title: TUPVCS_DT_Digitacao_Nota_Falta_WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPVCS_DT_Digitacao_Nota_Falta_WebService
version: 116
---

# Manipulação de Notas/Faltas de etapas de alunos

|  |  |
| --- | --- |
| **Linha de Produto:** | *TOTVS* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Classis.NET* |
| **Função:** | *WebService TBC para Notas/Faltas* |
| **Situação/Requisito:** | *Digitação de Notas e Faltas de etapas através do WebService TBC (wsDataServer)* |
| **Solução/Implementação:** | *Foi realizado uma melhoria na qual possibilita a digitação de Notas e Faltas de Etapas através do WebService wsDataServer do TBC.*  *Abaixo estão alguns exemplos do XML dos parâmetros utilizados na ferramenta **SoapUI**:*  **DataServer**: EduAlunoEtapaData  **ReadRecord:**  <soap:Envelope xmlns:soap="<http://www.w3.org/2003/05/soap-envelope>" xmlns:br="<http://www.totvs.com.br/br/>">  <soap:Header/>  <soap:Body>  <br:ReadRecordAuth>  <!--Optional:-->  <br:DataServerName>EduAlunoEtapaData</br:DataServerName>  <!--Optional:-->  <br:PrimaryKey>1;1;N;618239;1744163</br:PrimaryKey>  <!--Optional:-->  <br:Contexto>CODCOLIGADA=1</br:Contexto>  <!--Optional:-->  <br:Usuario>mestre</br:Usuario>  <!--Optional:-->  <br:Senha>totvs</br:Senha>  </br:ReadRecordAuth>  </soap:Body> </soap:Envelope>  O parâmetro **PrimeryKey** consiste nos seguintes valores separados por ponto e vírgula, nesta ordem: Código da Coligada, Código da Etapa, Tipo da Etapa, ID da Turma/Disciplina e RA do aluno.  **ReadView:**  <soap:Envelope xmlns:soap="<http://www.w3.org/2003/05/soap-envelope>" xmlns:br="<http://www.totvs.com.br/br/>">  <soap:Header/>  <soap:Body>  <br:ReadViewAuth>  <!--Optional:-->  <br:DataServerName>EduAlunoEtapaData</br:DataServerName>  <!--Optional:-->  <br:Filtro>SMATRICULA.IDTURMADISC=618239 AND SMATRICULA.RA=1744163</br:Filtro>  <!--Optional:-->  <br:Contexto>CODCOLIGADA=1</br:Contexto>  <!--Optional:-->  <br:Usuario>mestre</br:Usuario>  <!--Optional:-->  <br:Senha>totvs</br:Senha>  </br:ReadViewAuth>  </soap:Body> </soap:Envelope>  O parâmetro **Filtro** deverá ser uma string que será concatenada ao filtro da consulta existente no ReadView do dataserver EduAlunoEtapaData.  **SaveRecord:**  <soap:Envelope xmlns:soap="<http://www.w3.org/2003/05/soap-envelope>" xmlns:br="<http://www.totvs.com.br/br/>">  <soap:Header/>  <soap:Body>  <br:SaveRecordAuth>  <!--Optional:-->  <br:DataServerName>EduAlunoEtapaData</br:DataServerName>  <!--Optional:-->  <br:XML>  <![CDATA[ <SNotaEtapa>  <CODCOLIGADA>1</CODCOLIGADA>  <CODETAPA>1</CODETAPA>  <TIPOETAPA>N</TIPOETAPA>  <IDTURMADISC>618239</IDTURMADISC>  <RA>1744163</RA>  <NOTAFALTA>9</NOTAFALTA>  </SNotaEtapa>]]>  </br:XML>  <!--Optional:-->  <br:Contexto>CODCOLIGADA=1</br:Contexto>  <!--Optional:-->  <br:Usuario>mestre</br:Usuario>  <!--Optional:-->  <br:Senha>totvs</br:Senha>  </br:SaveRecordAuth>  </soap:Body> </soap:Envelope>    **Exemplo do XML para Notas:**  <SNotaEtapa>  <CODCOLIGADA>1</CODCOLIGADA>  <CODETAPA>1</CODETAPA>  <TIPOETAPA>N</TIPOETAPA>  <IDTURMADISC>1028</IDTURMADISC>  <RA>ES-00178</RA>  <NOTAFALTA>8</NOTAFALTA>  </SNotaEtapa>    **Exemplo XML para Faltas:**  <SNotaEtapa>  <CODCOLIGADA>1</CODCOLIGADA>  <CODETAPA>2</CODETAPA>  <TIPOETAPA>F</TIPOETAPA>  <IDTURMADISC>1028</IDTURMADISC>  <RA>ES-00178</RA>  <NOTAFALTA>8</NOTAFALTA>  </SNotaEtapa> |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |

divs
